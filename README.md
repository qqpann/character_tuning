# Python ChatGPT template

```sh
cp .env.example .env
vi .env # fill in your api key and organization id
pip install -r requirements.txt
python run.py
```

## Advanced hints

You may want to specify PYTHONPATH in some cases if you replace the model with your package.

```sh
PYTHONPATH=./models/your_model python run.py
```
