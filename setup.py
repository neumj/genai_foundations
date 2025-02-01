from setuptools import setup

reqs = ["loguru",]
test_pkgs = ["pytest", "coverage"]
develop_pkgs = ["jupyterlab"]

setup(
    name="gaif",
    packages=["gaif"],
    package_dir={"": "src"},
    version="0.0.1",
    python_requires=">3.11",
    description="Generative AI foundations.",
    url="https://github.com/neumj/genai_foundations",
    install_requires=reqs,
    extras_require={"develop": develop_pkgs, "test": test_pkgs},
    include_package_data=True,
    entry_points={"console_scripts": ["gaif = gaif.gaif_cli:start"]},
)
