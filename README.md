# API de Previsão de Renda

Para iniciar a API, execute o comando abaixo:

```bash
uvicorn main:app --reload
```

Quando o servidor estiver ativo, acesse a documentação da API em:

http://127.0.0.1:8000/docs

## Exemplo de Payload da Requisição

Abaixo está um exemplo de payload JSON que pode ser enviado para a API no endpoint `POST /predict`. Cada objeto representa uma pessoa, com características como idade, escolaridade, estado civil, ocupação, horas trabalhadas por semana e ganho de capital. A API retorna `0` (renda <=50K) ou `1` (renda >50K).

```json
{
  "data": [
    {
      "age": 25,
      "education_num": 1.0,
      "marital_status": "Never-married",
      "occupation": "Handlers-cleaners",
      "hours_per_week": 30.0,
      "capital_gain": 0.0
    },
    {
      "age": 40,
      "education_num": 13.0,
      "marital_status": "Married-civ-spouse",
      "occupation": "Prof-specialty",
      "hours_per_week": 50.0,
      "capital_gain": 10000.0
    },
    {
      "age": 30,
      "education_num": 9.0,
      "marital_status": "Divorced",
      "occupation": "Sales",
      "hours_per_week": 40.0,
      "capital_gain": 0.0
    },
    {
      "age": 50,
      "education_num": 16.0,
      "marital_status": "Married-civ-spouse",
      "occupation": "Exec-managerial",
      "hours_per_week": 60.0,
      "capital_gain": 5000.0
    },
    {
      "age": 22,
      "education_num": 7.0,
      "marital_status": "Never-married",
      "occupation": "Other-service",
      "hours_per_week": 20.0,
      "capital_gain": 0.0
    }
  ]
}
```

### Explicação dos Exemplos

- **Primeiro**: Educação muito baixa (`education_num=1.0`, ensino fundamental incompleto), solteiro, trabalha em limpeza, 30 horas/semana, sem ganho de capital. **Espera-se**: `0` (renda <=50K).
- **Segundo**: Educação alta (`education_num=13.0`, graduação), casado, profissão especializada, 50 horas/semana, alto ganho de capital. **Espera-se**: `1` (renda >50K).
- **Terceiro**: Educação média (`education_num=9.0`, ensino médio), divorciado, vendas, 40 horas/semana. **Espera-se**: `0` ou `1`.
- **Quarto**: Educação muito alta (`education_num=16.0`, doutorado), casado, gerente, 60 horas/semana, ganho de capital moderado. **Espera-se**: `1`.
- **Quinto**: Educação baixa (`education_num=7.0`, ensino fundamental completo), solteiro, serviços gerais, 20 horas/semana. **Espera-se**: `0`.

### Valores Válidos

- **age**: Número (ex.: 22, 50).
- **education_num**: Número de 1.0 a 16.0:
  - 1.0: Ensino fundamental incompleto.
  - 7.0: Ensino fundamental completo.
  - 9.0: Ensino médio completo.
  - 13.0: Graduação universitária.
  - 16.0: Doutorado.
- **marital_status**: `Never-married`, `Married-civ-spouse`, `Divorced`, `Widowed`, etc.
- **occupation**: `Handlers-cleaners`, `Prof-specialty`, `Sales`, `Exec-managerial`, `Other-service`, etc.
- **hours_per_week**: Número (ex.: 20.0, 60.0).
- **capital_gain**: Número (ex.: 0.0, 10000.0).
