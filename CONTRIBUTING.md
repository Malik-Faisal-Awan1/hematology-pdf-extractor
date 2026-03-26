# Contributing to Hematology PDF Data Extractor

First off, thank you for considering contributing to this project! 🎉

The following is a set of guidelines for contributing to the Hematology PDF Data Extractor. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Style Guidelines](#style-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

## 🤝 Code of Conduct

This project and everyone participating in it is governed by our commitment to be welcoming, friendly, and professional. By participating, you are expected to uphold this standard.

## 🎯 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the problem
- **Expected vs actual behavior**
- **Sample PDF** (if possible, anonymized)
- **Python version** and operating system
- **Full error traceback**

**Example Bug Report:**
```markdown
Title: HbF extraction fails for Lab X format

Description:
HbF values are not extracted from reports from Lab X in Karachi.

Steps to Reproduce:
1. Process PDF from Lab X
2. Check output CSV
3. HbF column is empty

Expected: HbF value extracted
Actual: Empty HbF field

Environment:
- Python 3.10
- Windows 11
- pdfplumber 0.10.3
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use case** - Why is this enhancement needed?
- **Proposed solution** - How should it work?
- **Alternatives considered**
- **Impact** - Who benefits from this?

### Adding New Lab Format Support

This is one of the most valuable contributions! To add support for a new lab format:

1. **Provide sample PDFs** (with patient data anonymized)
2. **Document the format** - where fields are located
3. **Update extraction patterns** in the code
4. **Add to location database** if needed
5. **Test thoroughly** with multiple samples
6. **Update documentation**

**Example:**
```python
# Add to LOCATION_DB
'New Lab Name': ('City', 'Province'),

# Document extraction pattern
# HbF appears on line 15, format: "Hb F: X.X %"
```

### Improving Documentation

Documentation improvements are always welcome:

- Fix typos or unclear explanations
- Add examples and use cases
- Improve installation instructions
- Create tutorials or guides
- Translate documentation

### Contributing Code

1. **Fork** the repository
2. **Create a branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes** following our style guidelines

4. **Test your changes**:
   ```bash
   # Run extraction on sample PDFs
   python pdf_extractor_final.py --input tests/sample_pdfs
   
   # Check output is correct
   ```

5. **Commit your changes** with clear messages

6. **Push** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**

## 📝 Style Guidelines

### Python Code Style

We follow [PEP 8](https://pep8.org/) with some additions:

```python
# Good ✅
def extract_hemoglobin_value(hb_type: str, text: str) -> str:
    """
    Extract hemoglobin fraction values.
    
    Args:
        hb_type: Type of hemoglobin (A, F, A2, etc.)
        text: Extracted PDF text
        
    Returns:
        Hemoglobin value as string, or empty string if not found
    """
    pattern = rf'\bHb\s+{re.escape(hb_type)}\b.*?%\s*([\d.]+)'
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1) if match else ''

# Bad ❌
def getHb(t,txt):
    p=rf'\bHb\s+{re.escape(t)}\b.*?%\s*([\d.]+)'
    m=re.search(p,txt,re.IGNORECASE|re.DOTALL)
    return m.group(1) if m else ''
```

**Key Points:**
- Use descriptive variable names
- Add docstrings to functions
- Type hints for function parameters
- Comments for complex logic
- Maximum line length: 100 characters
- 4 spaces for indentation (no tabs)

### Documentation Style

- Use **Markdown** for all documentation
- Include **code examples** where relevant
- Add **screenshots** for visual features
- Keep **language clear** and professional
- Use **emoji sparingly** for visual scanning

## 💬 Commit Messages

Write clear, descriptive commit messages:

### Format:
```
<type>: <subject>

<body (optional)>

<footer (optional)>
```

### Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code formatting (no logic change)
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Build/tool changes

### Examples:

**Good ✅**
```
feat: add support for XYZ Lab format

- Added extraction patterns for XYZ Lab reports
- Updated location database with XYZ branches
- Added test cases for new format

Resolves #42
```

**Good ✅**
```
fix: HbF extraction failing on multi-page PDFs

Previous regex was only searching first page. Updated to
search entire document text.

Fixes #38
```

**Bad ❌**
```
fixed stuff
```

**Bad ❌**
```
update
```

## 🔄 Pull Request Process

1. **Update documentation** if you changed functionality
2. **Add tests** if you added features
3. **Ensure all tests pass**
4. **Update CHANGELOG.md** with your changes
5. **Reference relevant issues** in the PR description

### PR Title Format:
```
[Type] Brief description

Examples:
[Feature] Add support for ABC Lab format
[Fix] Resolve HbF extraction issue
[Docs] Improve installation guide
```

### PR Description Template:
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing Done
- [ ] Tested with sample PDFs
- [ ] Verified output accuracy
- [ ] Checked edge cases

## Related Issues
Fixes #(issue number)

## Screenshots (if applicable)
```

## 🧪 Testing Guidelines

Before submitting:

1. **Test with real PDFs** (anonymized)
2. **Check all 37 fields** are extracted correctly
3. **Verify edge cases**:
   - Empty fields
   - Unusual values
   - Different date formats
   - Multi-page documents
4. **Test error handling**
5. **Check performance** (no significant slowdown)

## 📚 Adding to Documentation

When adding features:

1. Update **README.md** if it's a major feature
2. Add details to appropriate doc in `docs/`
3. Include **code examples**
4. Add to **CHANGELOG.md**

## 🏆 Recognition

Contributors will be acknowledged in:
- README.md Contributors section
- CHANGELOG.md for their contributions
- GitHub Contributors page

## 💡 Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/hematology-pdf-extractor.git
cd hematology-pdf-extractor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/
```

## 📞 Questions?

- Open an issue for questions
- Start a discussion in GitHub Discussions
- Check existing issues/PRs for similar topics

## 🎉 Thank You!

Your contributions make this project better for everyone in the healthcare community. Thank you for taking the time to contribute!

---

**Remember:** No contribution is too small. Even fixing a typo helps! 🌟
