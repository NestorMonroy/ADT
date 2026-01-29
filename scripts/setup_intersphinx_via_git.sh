#!/bin/bash
# Descarga inventarios intersphinx clonando repositorios con sparse checkout.
# Uso:
#   bash scripts/setup_intersphinx_via_git.sh

set -euo pipefail

DOWNLOAD_DIR="tools/_downloads"

clone_sparse() {
    local name="$1"
    local url="$2"
    local sparse_path="$3"
    local output_path="${DOWNLOAD_DIR}/${name}"

    if [ -d "${output_path}/.git" ]; then
        echo "Actualizando ${name}..."
        git -C "${output_path}" pull --depth 1 || true
        return 0
    fi

    echo "Clonando ${name}..."
    git clone --depth 1 --filter=blob:none --sparse "${url}" "${output_path}"
    if [ "${sparse_path}" != "." ]; then
        git -C "${output_path}" sparse-checkout set "${sparse_path}"
    fi
}

mkdir -p "${DOWNLOAD_DIR}"

clone_sparse "cpython" "https://github.com/python/cpython.git" "Doc"
clone_sparse "sphinx" "https://github.com/sphinx-doc/sphinx.git" "doc"

echo ""
echo "Inventarios esperados:"
echo "  - ${DOWNLOAD_DIR}/cpython/Doc/objects.inv"
echo "  - ${DOWNLOAD_DIR}/sphinx/doc/objects.inv"
