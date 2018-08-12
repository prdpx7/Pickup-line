from setuptools import setup

setup(name="pickupline",
      version="2.0",
      description="Get PickupLines on various categories from web",
      url="http://github.com/prdpx7/pickup-line",
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
          "html5lib",
      ],
      zip_safe=False)

