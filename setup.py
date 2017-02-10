from setuptools import setup

setup(name="pickupline",
      version="1.0",
      description="Get PickupLines on various categories from web",
      url="http://github.com/zuck007/pickup-line",
      author="Pradeep Khileri",
      author_email="pradeepchoudhary009@gmail.com",
      license="MIT",
      packages=["pickupline"],
      scripts=["./bin/pickup-line"],
      keywords='cli pickupline humour geek',
      install_requires=[
          "pyperclip",
          "requests",
          "bs4",
      ],
      zip_safe=False)

