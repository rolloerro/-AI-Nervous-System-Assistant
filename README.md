# 🧠 AI Nervous System Assistant

Экспериментальный AI-микросервис для анализа тревожного состояния человека.

Проект демонстрирует концепцию:

> AI как внешний модуль нервной системы человека.

---

## ⚡ Что делает сервис

Минимальный FastAPI endpoint:

* принимает текст
* анализирует эмоциональное состояние
* возвращает AI-ответ
* отдает JSON

---

## 🚀 Endpoint

POST `/analyze`

### Пример запроса

```json
{
  "text": "Мне тревожно по вечерам и сложно успокоиться"
}
```

### Пример ответа

```json
{
  "status": "ok",
  "analysis": "Похоже на тревожное перенапряжение нервной системы. Попробуйте снизить информационную нагрузку и переключить внимание на дыхание."
}
```

---

## 🛠 Stack

* FastAPI
* OpenAI API
* Python 3.12
* Uvicorn

---

## ⚠️ Важно

Проект НЕ является медицинской системой диагностики.

Это экспериментальный AI-assistant для:

* исследований
* UX-концепций
* AI wellness
* biohacking ideas
* nervous system interfaces

---

## 💡 Идея проекта

Мы постепенно подходим к точке,
где AI становится продолжением человеческой нервной системы:

* анализ состояния
* эмоциональная стабилизация
* когнитивная поддержка
* цифровые помощники

Будущее человек + AI уже начинается.

---

## ▶️ Запуск

```bash
pip install -r requirements.txt
```

```bash
uvicorn app:app --reload
```

Swagger UI:

```bash
http://127.0.0.1:8000/docs
```

---

## 👨‍💻 Author

Experimental microservice by:

https://github.com/rolloerro

----------------------------------------

🧠 AI Nervous System Assistant

Experimental AI microservice built with FastAPI + OpenAI.

A minimal AI-powered nervous system assistant prototype.

⚡ Features
/analyze endpoint
AI response generation
JSON output
FastAPI backend
OpenAPI docs
Lightweight microservice architecture
🚀 Quick Start
Install dependencies
pip install -r requirements.txt
Create .env
OPENAI_API_KEY=your_api_key_here
Run service
python -m uvicorn app:app --reload

Open docs:

http://127.0.0.1:8000/docs
📡 Example Request

POST /analyze

{
  "text": "I feel anxious in the evenings"
}
🧠 Example Response
{
  "result": "Your nervous system may be overloaded. Try reducing stimulation and focus on recovery."
}
⚠️ Disclaimer

This project is an experimental AI assistant and does not provide medical diagnosis.

Always consult healthcare professionals for medical concerns.

🔬 Tech Stack
FastAPI
OpenAI API
Python
Uvicorn
🌍 Vision

AI microservices are becoming a new interface layer between humans and intelligent systems.

This repository demonstrates how lightweight AI tools can be deployed in minutes and adapted for healthcare, biohacking, mental wellness, and educational applications.

👨‍💻 Author

Experimental AI architecture by:

https://github.com/rolloerro
