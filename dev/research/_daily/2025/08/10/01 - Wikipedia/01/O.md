# Спецификация `᛭O`
## 1.
### 1.1.
`Wi`: ⠿~ (статьи Википедии)

### 1.2.
`Wi-S` ≔ 
```
Понятие, которое описывает `Wi`.
Оно обозначено в заголовке `Wi`.
```

### 1.3.
`Wi-A` ≔ (URL `Wi`)

## 2.
### 2.1.
`G` ≔ 
```
name: Gemini
article: https://en.wikipedia.org/wiki/Gemini_(language_model)
```

### 2.2.
`Gn` ≔ 
```
Часть определения `G` с ключом `name`:
~~~
name: Gemini
~~~
```

### 2.3.
⊤ («Gemini» в `Gn` — это `Wi-S`)

### 2.4.
`Ga` ≔ 
```
Часть определения `G` с ключом `article`:
~~~
article: https://en.wikipedia.org/wiki/Gemini_(language_model)
~~~
```

### 2.5.
⊤ («https://en.wikipedia.org/wiki/Gemini_(language_model)» в `Ga` — это `Wi-A`)

## 3.
`Gi` : ⠿~
``
Правила типа `G`.
Они содержат `Gn` и `Ga`. 
```