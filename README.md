# 🧠 FlashForge - AI-Powered Flashcard & Quiz Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/Node.js-v14+-green.svg)](https://nodejs.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-brightgreen.svg)](https://www.mongodb.com/cloud/atlas)

## 📚 Overview

FlashForge is an intelligent learning platform that uses AI to generate personalized flashcards and quizzes based on topics or images. Perfect for students, educators, and lifelong learners, FlashForge helps reinforce knowledge through automated quiz generation and spaced repetition learning.

![FlashForge Logo](https://github.com/AdityaAjithKumar/FlashForge/blob/main/home.png)

## ✨ Features

- 🤖 **AI-Powered Content Generation**: Generate quizzes and flashcards from text topics or uploaded images
- 🖼️ **Image Analysis**: Extract content from images to create learning materials
- 🔐 **Secure Authentication**: User accounts with JWT authentication
- 💾 **Personal Library**: Save and manage your quizzes and flashcards
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile devices
- 🌐 **RESTful API**: Well-structured backend for easy integration

## 🖥️ Screenshots

### Quiz Interface
![Quiz Screenshot](https://github.com/AdityaAjithKumar/FlashForge/blob/main/quiz.jpeg)

### Flashcard Interface
![Flashcard Screenshot](https://raw.githubusercontent.com/AdityaAjithKumar/FlashForge/refs/heads/main/flash_card_front.jpeg)
![Flashcard Screenshot](https://raw.githubusercontent.com/AdityaAjithKumar/FlashForge/refs/heads/main/flash_card_back.jpeg)


## 🔄 System Architecture


![Flashcard Screenshot](https://raw.githubusercontent.com/AdityaAjithKumar/FlashForge/refs/heads/main/flowchat.jpeg)


## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Node.js, Express
- **Database**: MongoDB with Mongoose
- **Authentication**: JWT, Bcrypt
- **AI Services**: 
  - OpenAI's GPT-3.5 for quiz/flashcard generation
  - Google's Gemini for image analysis
- **File Handling**: Multer

## 🚀 Getting Started

### Prerequisites

- Node.js v14 or higher
- MongoDB Atlas account
- OpenAI API key
- Google Gemini API key

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```
PORT=3000
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret
API_KEY=your_openai_api_key
BASE_URL=https://api.openai.com/v1
GEMINI_API_KEY=your_gemini_api_key
```

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/AdityaAjithKumar/FlashForge
   cd flashforge
   ```

2. Install dependencies
   ```bash
   npm install
   ```

3. Start the server
   ```bash
   npm start
   ```

4. Visit `http://localhost:3000` in your browser

## 📋 API Endpoints

### Authentication
- `POST /register` - Register a new user
- `POST /login` - Log in and receive JWT token
- `POST /logout` - Log out

### Quiz Management
- `POST /generate-quiz` - Generate a new quiz
- `GET /user-quizzes` - Get all quizzes for the logged-in user
- `GET /quiz/:quizId` - Get a specific quiz

### Flashcard Management
- `POST /generate-flashcards` - Generate new flashcards
- `GET /user-flashcards` - Get all flashcards for the logged-in user
- `GET /flashcard/:flashcardId` - Get a specific flashcard set

### Image Analysis
- `POST /analyze-image` - Analyze an uploaded image

## 📚 Usage Examples

### Generate a Quiz

```javascript
// Example: Creating a quiz about astronomy
fetch('/generate-quiz', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_JWT_TOKEN'
  },
  body: JSON.stringify({
    topic: 'astronomy',
    number: 5
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

### Generate Flashcards from an Image

```javascript
// Example: Creating flashcards from an uploaded image
const formData = new FormData();
formData.append('image', imageFile);
formData.append('number', 10);

fetch('/generate-flashcards', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_JWT_TOKEN'
  },
  body: formData
})
.then(response => response.json())
.then(data => console.log(data));
```

## 🧩 Models

### User Model
```javascript
{
  username: String,
  email: String,
  password: String,
  quizzes: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Quiz' }],
  flashcards: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Flashcard' }]
}
```

### Quiz Model
```javascript
{
  title: String,
  questions: [{
    question: String,
    options: [String],
    answer: String
  }],
  user: { type: mongoose.Schema.Types.ObjectId, ref: 'User' }
}
```

### Flashcard Model
```javascript
{
  title: String,
  flashcards: [{
    term: String,
    definition: String
  }],
  user: { type: mongoose.Schema.Types.ObjectId, ref: 'User' }
}
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAI for providing the GPT-3.5 API
- Google for the Gemini API
- MongoDB Atlas for database hosting
- All contributors and supporters of this project
