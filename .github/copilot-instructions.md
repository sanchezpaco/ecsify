# GitHub Copilot Instructions for ECSify

## 🚨 CRITICAL RULES - NEVER BREAK THESE

### 1. Documentation First
- **ALWAYS** read `SYSTEM_DESIGN.md` and `ROADMAP.md` before starting any task
- **NEVER** implement features not specified in these documents
- **ALWAYS** ask the user if anything is unclear or ambiguous

### 2. Test-Driven Development & Behaviour Driven Development (TDD/BDD)
- **ALWAYS** run existing tests before implementing new features
- **ALWAYS** write tests first, then implement code
- **NEVER** commit code without tests
- **ALWAYS** maintain >90% test coverage

### 3. Quality Gates
Every task completion must pass ALL these gates:
- [ ] All tests pass (unit + integration)
- [ ] Code coverage >90%
- [ ] Documentation updated
- [ ] Examples work correctly
- [ ] Manual testing completed by user
- [ ] Conventional commit made

### 4. Communication Style
- **ALWAYS** maintain a neutral and direct tone
- **NEVER** use overly enthusiastic or casual language
- **ALWAYS** be concise and professional in responses
- **NEVER** use emojis or excessive punctuation in code or technical communication

---

## 📋 Workflow Rules

### Before Starting Any Task
1. Run all existing tests: `make test` or `pytest`
2. Ensure tests are green
3. Read relevant sections in SYSTEM_DESIGN.md and ROADMAP.md
4. If unclear, **STOP and ASK the user**

### During Development
1. **Write tests first** (TDD approach)
2. Implement minimal code to make tests pass
3. Refactor and improve
4. Update documentation
5. Create/update examples

### After Completing Each Task
1. Run full test suite
2. Verify code coverage >90%
3. Test examples manually
4. Update relevant documentation
5. Make conventional commit
6. **User performs manual testing**

---

## 🌿 Branch Convention

Use simple, descriptive branch names without prefixes:

### Main Phase Branches
```
core-cli
environment-support
ux-improvements
advanced-features
```

### Subtask Branches (if needed)
```
project-setup
pydantic-models
yaml-parsing
aws-client
deployment-logic
cli-interface
dry-run
```

### Branch Workflow
1. Create branch from `main`: `git checkout -b core-cli`
2. Work on the branch
3. Make conventional commits
4. User creates PR to `main`

---

## 📝 Commit Convention

Use [Conventional Commits](https://www.conventionalcommits.org/) format:

### Format
```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Adding or modifying tests
- `refactor`: Code refactoring
- `style`: Code style changes
- `chore`: Build process or auxiliary tool changes

### Examples
```bash
feat(cli): add basic apply command with click framework
feat(models): implement pydantic validation for task definitions
test(aws): add integration tests for ECS client operations
docs(readme): add installation and usage examples
fix(parser): handle YAML syntax errors gracefully
refactor(deployer): extract deployment status monitoring
```

### Scope Guidelines
- `cli`: Command-line interface
- `models`: Pydantic data models
- `parser`: YAML parsing and validation
- `aws`: AWS client operations
- `deploy`: Deployment logic
- `utils`: Utility functions
- `docs`: Documentation
- `tests`: Test-related changes

---

## 🧪 Testing Requirements

### Test Categories
1. **Unit Tests**: Test individual functions/classes
2. **Integration Tests**: Test AWS operations (mocked)
3. **End-to-End Tests**: Test complete workflows
4. **CLI Tests**: Test command-line interface

### Coverage Requirements
- **Minimum**: 90% overall coverage
- **Target**: 95% coverage
- **Critical paths**: 100% coverage (deployment, validation)

### Test Structure
```
tests/
├── unit/
│   ├── test_models.py
│   ├── test_parser.py
│   └── test_utils.py
├── integration/
│   ├── test_aws_client.py
│   └── test_deployment.py
├── e2e/
│   └── test_full_workflow.py
└── cli/
    └── test_commands.py
```

---

## 📚 Documentation Requirements

### Always Update
- README.md (if user-facing changes)
- Docstrings (all public functions/classes)
- Type hints (all functions)
- Examples (if new features)
- CHANGELOG.md (for releases)

### Documentation Standards
- Use clear, concise language
- Include code examples
- Add error handling examples
- Document all parameters and return values
- Include usage examples in docstrings

---

## 🔍 Code Quality Standards

### Python Standards
- Follow PEP 8
- Use type hints everywhere
- Maximum line length: 88 characters (black default)
- Use meaningful variable names
- Add docstrings to all public functions
- **IMPORTANT: NO COMMENTS IN CODE - CODE IS EXPLAINED BY TESTS**

### Error Handling
- Use custom exception hierarchy from `utils/exceptions.py`
- Provide clear, actionable error messages
- Include context in error messages
- Handle AWS API errors gracefully

### Logging
- Use rich console logging from `utils/logger.py`
- Log at appropriate levels (DEBUG, INFO, WARNING, ERROR)
- Include timestamps and context
- No sensitive information in logs

---

## 🚦 Quality Checklist

Before marking any task as complete:

### Code Quality
- [ ] All functions have type hints
- [ ] All public functions have docstrings
- [ ] Code follows PEP 8 standards
- [ ] No hardcoded values (use constants/config)
- [ ] Error handling is comprehensive

### Testing
- [ ] All new code has tests
- [ ] Tests cover both success and failure cases
- [ ] Integration tests use mocked AWS calls
- [ ] CLI tests verify all command options
- [ ] Coverage is >90%

### Documentation
- [ ] README updated if needed
- [ ] Docstrings added/updated
- [ ] Examples created/updated
- [ ] Tests explain code behavior clearly
- [ ] Type hints are accurate

### Functionality
- [ ] Feature works as specified in SYSTEM_DESIGN.md
- [ ] Follows patterns from ROADMAP.md
- [ ] Integrates with existing code
- [ ] Handles edge cases gracefully
- [ ] Performance is acceptable

---

## ❌ What NOT to Do

### Never Do These
- **Don't** implement features not in SYSTEM_DESIGN.md
- **Don't** commit without tests
- **Don't** commit with failing tests
- **Don't** skip documentation updates
- **Don't** hardcode AWS credentials
- **Don't** ignore error cases
- **Don't** assume - always ask if unclear
- **Don't** add comments in code - let tests explain the behavior

### Anti-Patterns to Avoid
- Overly complex abstractions
- Tight coupling between modules
- Missing error handling
- Poor test coverage
- Unclear variable names
- Magic numbers/strings
- Silent failures

---

## 🆘 When in Doubt

### Always Ask the User About
- Unclear requirements
- Implementation approaches
- API design decisions
- Error handling strategies
- Testing strategies
- Performance considerations

### Format for Questions
```
🤔 **Question about [topic]**

**Context**: [what you're working on]
**Issue**: [what's unclear]
**Options**: [if you have alternatives]
**Recommendation**: [your suggested approach]

Should I proceed with [recommendation] or would you prefer a different approach?
```

---

## 🎯 Success Criteria

### Task Completion
A task is only complete when:
- All code is tested (>90% coverage)
- Documentation is updated
- Examples work correctly
- User has performed manual testing
- Conventional commit is made
- All quality gates pass

### Phase Completion
A phase is complete when:
- All phase tasks are complete
- Integration testing passes
- User acceptance testing passes
- Documentation is comprehensive
- Examples demonstrate all features

Remember: **Quality over speed**. It's better to complete fewer tasks well than many tasks poorly.
