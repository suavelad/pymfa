import setuptools


setuptools.setup(     
     name="sub-module",     
     version="0.0.1",
     description="This helps you setup MFA with 3rd Party Authenticator",
     python_requires=">=3.10",   
     packages=["mfa-authenticator"],
     install_requires=["python-decouple","pyotp","qrcode"],

)