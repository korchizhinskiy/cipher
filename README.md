# Дешифратор шифра Цезаря

## Развертывание проекта локально

```
git clone https://github.com/korchizhinskiy/cipher.git
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Запуск проекта

### Unicorn
```sudo uvicorn app.main:app --host 0.0.0.0 --port 80 --reload```

### Docker
```
docker build -t cipher .
docker run -p 80:80 cipher
```
