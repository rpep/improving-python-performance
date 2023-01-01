from setuptools import Extension, setup

extra_compile_args = ["-O2", "-march=native", "-fopenmp"]
extra_link_args = ["-fopenmp"]

setup(
    ext_modules=[
        Extension(
            name="mathematical_routines.cfunctions",
            sources=["mathematical_routines/functions.c", "mathematical_routines/cfunctions.pyx"],
            extra_compile_args=extra_compile_args,
            extra_link_args=extra_link_args,
        ),
    ]
)
