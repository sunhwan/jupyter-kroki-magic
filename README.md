# Jupyter Kroki Magic

A Jupyter Notebook %%magic for drawing diagrams using kroki.io or self-hosted kroki server.

URL is read from args first, then environment var `KROKI_ENDPOINT` is checked and last fallback to `https://kroki.io`.

Additionally variable expansion within diagram syntax can be enabled, to reuse content of other cells as well.

Usage
------

Load extension inside a Jupyter notebook:

```
%load_ext krokimagic
```

Add code with Cell magic:

```
%%kroki [diagram-type]

# diagram syntax
```

for help and usage, see also
```
%%kroki?
```

Examples
--------

```
%%kroki plantuml

skinparam monochrome true
skinparam ranksep 20
skinparam dpi 150
skinparam arrowThickness 0.7
skinparam packageTitleAlignment left
skinparam usecaseBorderThickness 0.4
skinparam defaultFontSize 12
skinparam rectangleBorderThickness 1

rectangle "Main" {
  (main.view)
  (singleton)
}
rectangle "Base" {
  (base.component)
  (component)
  (model)
}
rectangle "<b>main.ts</b>" as main_ts

(component) ..> (base.component)
main_ts ==> (main.view)
(main.view) --> (component)
(main.view) ...> (singleton)
(singleton) ---> (model)
```

or

```
persons=['Alice','Bob']
```
```
%%kroki --expand_vars plantuml
@startuml
{persons[0]} -> {persons[1]}: Authentication Request
{persons[1]} --> {persons[0]}: Authentication Response

{persons[0]} -> {persons[1]}: Another authentication Request
{persons[0]} <-- {persons[1]}: Another authentication Response
@enduml
```
Installation
------------

    $ pip install jupyter-kroki-magic