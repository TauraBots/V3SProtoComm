from setuptools import setup, find_packages
import os
import glob
import subprocess
import sys
import re


# Função para compilar os arquivos .proto
def compile_proto_files():
    print("Compilando arquivos .proto...")

    # Verificar se protoc está instalado
    try:
        subprocess.check_output(["protoc", "--version"])
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("AVISO: protoc não encontrado. Os arquivos .proto não serão compilados.")
        return

    # Diretório base dos arquivos .proto
    proto_base_dir = os.path.join(
        "V3SProtoComm", "core", "comm", "protocols", "protobuf"
    )

    # Compilar command.proto e packet.proto primeiro
    main_proto_files = [
        os.path.join(proto_base_dir, "command.proto"),
        os.path.join(proto_base_dir, "packet.proto"),
    ]

    for proto_file in main_proto_files:
        if os.path.exists(proto_file):
            proto_dir = os.path.dirname(proto_file)
            output_dir = os.path.join("V3SProtoComm", "core", "comm", "protocols")
            cmd = [
                "protoc",
                "--proto_path=" + proto_dir,
                "--python_out=" + os.path.dirname(output_dir),
                proto_file,
            ]
            print(f"Executando: {' '.join(cmd)}")
            subprocess.call(cmd)

    # Compilar os arquivos .proto nas subpastas
    subdirs = ["firasim", "vision_proto", "vssreferee"]
    for subdir in subdirs:
        subdir_path = os.path.join(proto_base_dir, subdir)
        if os.path.exists(subdir_path):
            proto_files = glob.glob(os.path.join(subdir_path, "*.proto"))
            for proto_file in proto_files:
                output_dir = os.path.join("V3SProtoComm", "core", "comm", "protocols")
                cmd = [
                    "protoc",
                    "--proto_path=" + subdir_path,
                    "--python_out=" + output_dir,
                    proto_file,
                ]
                print(f"Executando: {' '.join(cmd)}")
                subprocess.call(cmd)

    # Corrigir as importações nos arquivos gerados
    pb2_files = glob.glob(
        os.path.join("V3SProtoComm", "core", "comm", "protocols", "*_pb2.py")
    )

    # Obter lista de todos os nomes de arquivos _pb2.py (sem a extensão)
    pb2_modules = [os.path.basename(f)[:-3] for f in pb2_files]
    print(f"Módulos _pb2 encontrados: {pb2_modules}")

    for pb2_file in pb2_files:
        print(f"Corrigindo importações em {pb2_file}...")
        with open(pb2_file, "r") as f:
            content = f.read()

        # Usar expressão regular para encontrar todas as importações de arquivos _pb2
        # Padrão: import nome_pb2 ou import nome_pb2 as nome__pb2
        import_pattern = r"import\s+(\w+_pb2)(?:\s+as\s+(\w+))?"

        # Encontrar todas as importações
        imports = re.findall(import_pattern, content)

        # Substituir cada importação encontrada
        for module, alias in imports:
            if alias:
                # Importação com alias: import nome_pb2 as nome__pb2
                old_import = f"import {module} as {alias}"
                new_import = f"from . import {module} as {alias}"
            else:
                # Importação simples: import nome_pb2
                old_import = f"import {module}"
                new_import = f"from . import {module}"

            print(f"  Substituindo '{old_import}' por '{new_import}'")
            content = content.replace(old_import, new_import)

        with open(pb2_file, "w") as f:
            f.write(content)

    print("Compilação dos arquivos .proto concluída.")


# Compilar os arquivos .proto antes da instalação
compile_proto_files()

setup(
    name="V3SProtoComm",
    version="2.1.0",
    description="Pacote para comunicação e controle de robôs via Protobuf",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Thassio",
    author_email="thxssio@gmail.com",
    url="https://github.com/Taurabots/V3SProtoComm",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "protobuf",  # Usar a versão do usuário
        "six",
        "toml",
        "wrapt",
    ],
    entry_points={
        "console_scripts": [
            "gotoball=gotoball:gotoball",
        ],
    },
)
