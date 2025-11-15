# 📊 Esquemas Visuais - Aula 01: Fundamentos Básicos de Sistemas Biológicos

## 1. Características dos Sistemas Vivos

```mermaid
mindmap
  root((Sistemas Vivos))
    Complexidade e Organização
      Estrutura hierárquica
      Moléculas → Organelas → Células
    Extração de Energia
      Fotossíntese
      Respiração celular
      Metabolismo
    Autorreplicação
      DNA como molde
      Transmissão genética
      Fidelidade na cópia
    Percepção e Resposta
      Sensores moleculares
      Transdução de sinais
      Adaptação ambiental
    Funções Reguladas
      Enzimas
      Feedback negativo/positivo
      Homeostase
    Evolução
      Seleção natural
      Mutação
      Adaptação
```

---

## 2. Os Três Domínios da Vida

```mermaid
graph TD
    A[Ancestral Universal Comum] --> B[Bactérias<br/>Eubacteria]
    A --> C[Arqueas<br/>Archaea]
    A --> D[Eucariotos<br/>Eukarya]
    
    B --> B1[E. coli]
    B --> B2[Cianobactérias]
    B --> B3[Streptococcus]
    
    C --> C1[Halófilas<br/>ambientes salinos]
    C --> C2[Termófilas<br/>fontes termais]
    C --> C3[Metanogênicas]
    
    D --> D1[Protistas]
    D --> D2[Fungos]
    D --> D3[Plantas]
    D --> D4[Animais]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

---

## 3. Dualidade: Complexidade Estrutural vs. Simplicidade Molecular

```mermaid
graph LR
    A[Moléculas Simples] --> B[Macromoléculas]
    B --> C[Complexos Supramoleculares]
    C --> D[Organelas]
    D --> E[Células]
    E --> F[Tecidos]
    F --> G[Órgãos]
    G --> H[Organismos]
    
    A1[20 Aminoácidos] -.-> B1[Proteínas<br/>400.000 Da]
    A2[4 Nucleotídeos] -.-> B2[DNA/RNA<br/>milhões de pares de bases]
    A3[Açúcares simples<br/>C4-C6] -.-> B3[Polissacarídeos<br/>celulose, amido]
    
    style A fill:#ffcccc
    style B fill:#ffddaa
    style C fill:#ffffaa
    style D fill:#ddffaa
    style E fill:#aaffaa
    style F fill:#aaffdd
    style G fill:#aaddff
    style H fill:#ccaaff
```

---

## 4. Composição Elementar da Vida

```mermaid
pie title Composição Elementar (% da massa celular)
    "Carbono (C)" : 50
    "Oxigênio (O)" : 20
    "Hidrogênio (H)" : 10
    "Nitrogênio (N)" : 14
    "Outros (P, S, K, Na, Ca, Mg)" : 6
```

---

## 5. Estrutura Básica de uma Célula Eucariótica

```mermaid
graph TB
    subgraph Célula[Célula Eucariótica]
        N[Núcleo<br/>Material Genético DNA]
        M[Mitocôndria<br/>Produção de ATP]
        RE[Retículo Endoplasmático<br/>Síntese de proteínas]
        G[Complexo de Golgi<br/>Processamento]
        R[Ribossomos<br/>Tradução]
        C[Citosol<br/>Íons + pequenas moléculas]
        MB[Membrana Plasmática<br/>Lipídios + Proteínas]
    end
    
    N -.DNA.-> R
    R -.Proteínas.-> RE
    RE --> G
    M -.ATP.-> C
    
    style N fill:#ffcccc
    style M fill:#ccffcc
    style RE fill:#ccccff
    style G fill:#ffffcc
    style R fill:#ffccff
    style C fill:#e6f3ff
    style MB fill:#ffe6cc
```

---

## 6. Abordagens de Estudo em Bioquímica

```mermaid
flowchart LR
    A[Sistema Biológico Complexo<br/>Mapa Metabólico] --> B{Enfoque Reducionista}
    
    B --> C[In Vitro<br/>no vidro]
    B --> D[In Vivo<br/>em vida]
    
    C --> C1[Isolar componentes]
    C1 --> C2[Estudar reações individuais]
    C2 --> C3[Análise quantitativa]
    
    D --> D1[Observar no organismo vivo]
    D1 --> D2[Contexto completo]
    D2 --> D3[Interações complexas]
    
    C3 --> E[Reconstruir o sistema completo]
    D3 --> E
    
    E --> F[Compreensão Integrada]
    
    style A fill:#ff9999
    style C fill:#99ccff
    style D fill:#99ff99
    style F fill:#ffcc99
```

---

## 7. Fluxo: Da Molécula ao Organismo

```mermaid
graph TD
    A[Átomos<br/>C, H, O, N] --> B[Moléculas Simples<br/>aminoácidos, nucleotídeos]
    B --> C[Macromoléculas<br/>proteínas, DNA, polissacarídeos]
    C --> D[Complexos Supramoleculares<br/>ribossomos, cromossomos]
    D --> E[Organelas<br/>núcleo, mitocôndrias]
    E --> F[Célula<br/>unidade básica da vida]
    F --> G[Tecido<br/>células especializadas]
    G --> H[Órgão<br/>funções integradas]
    H --> I[Sistema<br/>digestório, nervoso]
    I --> J[Organismo<br/>ser vivo completo]
    
    style A fill:#ffe6e6
    style B fill:#fff0e6
    style C fill:#fffae6
    style D fill:#f0ffe6
    style E fill:#e6ffe6
    style F fill:#e6fff0
    style G fill:#e6f9ff
    style H fill:#e6ecff
    style I fill:#ece6ff
    style J fill:#f9e6ff
```

---

## 8. Princípio Fundamental da Bioquímica

```mermaid
graph LR
    A[Moléculas Biológicas] --> B{Obedecem às mesmas leis}
    B --> C[Leis da Física]
    B --> D[Leis da Química]
    
    C --> E[Termodinâmica]
    C --> F[Mecânica Quântica]
    
    D --> G[Ligações Químicas]
    D --> H[Reações Químicas]
    
    E --> I[Não há quebra da<br/>1ª Lei da Termodinâmica]
    F --> I
    G --> I
    H --> I
    
    I --> J[Vida = Química Organizada]
    
    style A fill:#ffcccc
    style B fill:#ffffcc
    style C fill:#ccffcc
    style D fill:#ccccff
    style I fill:#ffccff
    style J fill:#ff9999
```

---

## Instruções para Visualização

Estes diagramas estão em formato **Mermaid**, que pode ser renderizado em:
- GitHub (suporte nativo)
- VS Code (com extensão Mermaid)
- Ferramentas online: [Mermaid Live Editor](https://mermaid.live/)

Para gerar imagens PNG, use o comando:
```bash
manus-render-diagram esquemas_aula01.md esquemas_aula01.png
```
