# 🤝 Contributing to Caelus

Thank you for your interest in contributing to Caelus! This document provides guidelines for contributing to the project.

## 🎯 Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/gmusic1007/caelus.git
   cd caelus
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install development dependencies**
   ```bash
   pip install -e ".[dev]"
   ```

## 🧪 Testing

Run the test suite:
```bash
pytest
```

Run with coverage:
```bash
pytest --cov=caelus --cov-report=html
```

## 📝 Code Style

We use:
- **Black** for code formatting
- **Flake8** for linting
- **Type hints** for better code documentation

Format your code:
```bash
black caelus/
flake8 caelus/
```

## 🔄 Development Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

3. **Test your changes**
   ```bash
   pytest
   black caelus/
   flake8 caelus/
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

5. **Push and create a pull request**
   ```bash
   git push origin feature/your-feature-name
   ```

## 📋 Pull Request Guidelines

- **Title**: Use conventional commit format (e.g., "feat: add ABC validation")
- **Description**: Clearly describe the changes and their purpose
- **Tests**: Ensure all tests pass
- **Documentation**: Update README or docstrings if needed

## 🎼 Musical Notation Guidelines

When working with ABC or MusicXML:

- **ABC Notation**: Follow the [ABC standard](https://abcnotation.com/)
- **MusicXML**: Ensure compatibility with major notation software
- **Validation**: Test with real musical examples
- **Edge Cases**: Handle unusual musical constructs gracefully

## 🐛 Bug Reports

When reporting bugs, please include:

- **Description**: Clear explanation of the issue
- **Reproduction**: Steps to reproduce the problem
- **Expected vs Actual**: What you expected vs what happened
- **Environment**: Python version, OS, dependencies
- **Sample Data**: ABC or MusicXML files that trigger the issue

## 💡 Feature Requests

For feature requests:

- **Use Case**: Explain why this feature is needed
- **Implementation**: Suggest how it might work
- **Priority**: Indicate if it's a nice-to-have or essential

## 📞 Questions?

Feel free to open an issue for questions or discussions about the project.

---

**♠️🌿🎸🧵 Thank you for contributing to the G.Music Assembly!** 