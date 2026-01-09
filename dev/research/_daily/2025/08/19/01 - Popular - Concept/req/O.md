# 1.
`O` ≔ (https://en.wikipedia.org/wiki/Ontology_(information_science))

# 2.
## 2.1.
`Ls` ≔ ⠿~ (https://en.wikipedia.org/wiki/Ontology_language)

## 2.2.
`Li` : `Ls`

# 3.
`K` ≔ (https://en.wikipedia.org/wiki/Class_(knowledge_representation))

# 4.
## 4.1.
`C1` ≔ (Термин «concept» для `K` в `Ls`)

## 4.2.
`C2` ≔ (Термин «class» для `K` в `Ls`)

# 5.
## 5.1.
`Cs` ≔ ⠿{`C1`, `C2`}

## 5.2.
`Ci` : `Cs`

# 6.
## 6.1.
`L1s` ≔ ⠿~ (`Li`, которые используют `C1`)

## 6.2.
`L1i` : `L1s`

## 6.3.
`L2s` ≔ ⠿~ (`Li`, которые используют `C2`)

## 6.4.
`L2i` : `L2s`

# 7.
`Mⰳ(i : Ls)` ≔ 
```
Метрика(мера) количества информации, содержащейся в твоей нейросети about `i`
```