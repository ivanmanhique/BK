import setuptools


long_description = "My long description"

setuptools.setup(
    name="BookingSystem",
    version="0.0.1",
    author="Jonatant",
    author_email="s24183@pjwstk.edu.pl",
    description="My short description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/shkroba/nonion",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "nonion==0.4.4",
        "SQLAlchemy"=="2.0.9",
        "psycopg2-binary"=="2.9.6",
        "pydantic"=="1.10.7"
    ],
)