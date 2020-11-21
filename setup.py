from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_reqs = f.read().splitlines()

setup(name="pickupline",
      version="3.0",
      description="Get PickupLines on various categories from web",
      url="http://github.com/prdpx7/pickup-line",
      author="Pradeep Khileri",
      author_email="pradeepchoudhary009@gmail.com",
      license="MIT",
      packages=find_packages(),
      scripts=['bin/pickup-line'],
      keywords='cli pickupline humour geek',
      install_requires=install_reqs,
      zip_safe=False)

