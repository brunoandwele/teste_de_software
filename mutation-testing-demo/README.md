# Mutation Testing Demo

Um projeto educacional demonstrando testes de mutação em Python usando a ferramenta `mutmut`.

## Sobre o Projeto

Este projeto foi desenvolvido para ensinar os conceitos de **testes de mutação** através de exemplos práticos. Os testes de mutação são uma técnica avançada que avalia a qualidade de uma suíte de testes introduzindo pequenas alterações (mutações) no código e verificando se os testes conseguem detectá-las.

## Estrutura do Projeto

```
mutation-testing-demo/
├── README.md
├── requirements.txt
├── setup.cfg
├── .github/
│   └── workflows/
│       └── mutation-tests.yml
├── calculator/
│   ├── __init__.py
│   └── operations.py
└── tests/
    ├── __init__.py
    └── test_operations.py
```

## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Git

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/mutation-testing-demo.git
   cd mutation-testing-demo
   ```

2. **Crie um ambiente virtual (recomendado):**
   ```bash
   python -m venv venv
   
   # Linux/Mac
   source venv/bin/activate
   
   # Windows
   venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## Como Usar

### 1. Executar Testes Normais

Primeiro, verifique se todos os testes passam:

```bash
python -m pytest tests/ -v
```

### 2. Verificar Cobertura de Código

```bash
python -m pytest --cov=calculator/ --cov-report=term-missing tests/
```

### 3. Executar Testes de Mutação

```bash
# Executar mutmut
mutmut run

# Ver resultados
mutmut results

# Analisar mutantes específicos
mutmut show 1
mutmut show 2
```

### 4. Interpretar Resultados

Os resultados do mutmut incluem:

- **Killed mutants**: Testes detectaram a mutação (bom!)
- **Survived mutants**: Testes não detectaram a mutação (precisa melhorar)
- **Timeout mutants**: Mutação causou execução muito lenta
- **Incompetent mutants**: Mutação causou erro de sintaxe

### 5. Calcular Taxa de Mutação

```python
killed = 30  # número de mutantes mortos
total = 34   # número total de mutantes
incompetent = 1  # número de mutantes incompetentes

valid_mutants = total - incompetent
mutation_score = (killed / valid_mutants) * 100
print(f'Taxa de Mutação: {mutation_score:.1f}%')
```

**Meta recomendada:** Taxa de mutação > 80%

## Funcionalidades da Calculadora

A classe `Calculator` implementa operações básicas:

- **Aritméticas**: soma, subtração, multiplicação, divisão, potenciação
- **Matemáticas**: raiz quadrada, fatorial
- **Utilitárias**: verificação de números pares

Cada função inclui tratamento de casos especiais e validação de entrada.

## Comandos Úteis

```bash
# Limpar cache do mutmut
mutmut cache clear

# Executar em arquivo específico
mutmut run --paths-to-mutate calculator/operations.py

# Aplicar mutante para teste manual
mutmut apply 2
python -m pytest tests/ -v
git checkout -- calculator/

# Exportar relatório
mutmut results > mutation_report.txt
```

## Integração Contínua

O projeto inclui workflow do GitHub Actions (`.github/workflows/mutation-tests.yml`) que:

- Executa testes unitários
- Executa testes de mutação
- Verifica se a taxa de mutação atende ao critério mínimo (80%)
- Gera relatórios automáticos

## Problemas Comuns

### Execução Lenta
```bash
mutmut run --runner-timeout 30
```

### Muitos Mutantes Incompetentes
```bash
python -m py_compile calculator/operations.py
```

### Testes Falhando
```bash
python -m pytest tests/ --tb=short
```

## Exemplo de Análise

### Antes da Melhoria
```
Killed mutants (25)
survived mutants (8)
timeout mutants (0)
incompetent mutants (1)
total mutants (34)

Taxa de Mutação: 75.8%
```

### Após Melhorias nos Testes
```
Killed mutants (32)
survived mutants (1)
timeout mutants (0)
incompetent mutants (1)
total mutants (34)

Taxa de Mutação: 97.0%
```

## Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Objetivos Educacionais

Este projeto ensina:

- Como implementar testes de mutação
- Diferença entre cobertura de código e qualidade de testes
- Identificação de lacunas em suítes de teste
- Uso prático da ferramenta mutmut
- Integração de testes de mutação em CI/CD

## Recursos Adicionais

- [Documentação do mutmut](https://mutmut.readthedocs.io/)
- [Artigo original sobre Mutation Testing](https://dl.acm.org/doi/10.1145/360248.360252)
- [Pytest Documentation](https://docs.pytest.org/)

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Autor

- **Prof. Luciano Rossi** - Centro Universitário FEI
- Disciplina: Simulação e Teste de Software (CC8550)

## Agradecimentos

- Comunidade Python pelo ecossistema de ferramentas de teste
- Desenvolvedores do mutmut pela excelente ferramenta
- Estudantes da FEI pelo feedback e sugestões