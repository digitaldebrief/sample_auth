
# sample_auth Flask Application

Awesome sample_auth created by digitaldebrief

## Installation

From source:

```bash
git clone https://github.com/digitaldebrief/sample_auth sample_auth
cd sample_auth
make install
```

From pypi:

```bash
pip install sample_auth
```

## Executing

This application has a CLI interface that extends the Flask CLI.

Just run:

```bash
$ sample_auth
```

or

```bash
$ python -m sample_auth
```

To see the help message and usage instructions.

## First run

```bash
sample_auth create-db   # run once
sample_auth populate-db  # run once (optional)
sample_auth add-user -u admin -p 1234  # ads a user
sample_auth run
```

Go to:

- Website: http://localhost:5000
- Admin: http://localhost:5000/admin/
  - user: admin, senha: 1234
- API GET:
  - http://localhost:5000/api/v1/product/
  - http://localhost:5000/api/v1/product/1
  - http://localhost:5000/api/v1/product/2
  - http://localhost:5000/api/v1/product/3


> **Note**: You can also use `flask run` to run the application.
