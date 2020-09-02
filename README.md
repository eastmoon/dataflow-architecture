# Dataflow architecture project

+ Research document
  - [Architecture pattern](https://github.com/eastmoon/research-software-theory/blob/master/software-engineering/architecture_pattern.md)
  - [Dataflow architecture](https://github.com/eastmoon/research-software-theory/blob/master/software-engineering/dataflow_architecture.md)
  - [Asynchronous execute](https://github.com/eastmoon/research-software-theory/blob/master/distribution-and-network/asynchronous-execute.md)

此專案是以樣式設計實踐流程架構概念，其設計主要思想來自於 Layer、Pipes & Filters

It is a project using design pattern to implement process architecture concept, which design idea come from Layer, Pipes & Filters.

依據 [Pattern-Oriented Software Architecture](https://www.amazon.com/Pattern-Oriented-Software-Architecture-System-Patterns/dp/0471958697) 定義，From Mud to Structure 在討論著如何將不同規範的系統，基於過往實務的經驗歸納出架構的定義，並以此延伸適用於新系統的基礎架構；然而細看這些定義，即可發現其定位在解釋系統流程上，處理資料、資訊傳遞、資料儲存的規範，從此中再參考 [Patterns of Enterprise Application Architecture](https://ihower.tw/blog/archives/1294) 內容，對此個人提出此類架構的統一概念。

此類架構主要是基於資料流 ( Dataflow ) 的處理程序進行架構化，然而依據不同程式設計範例 ( Programming Paradigm ) 以及應用範圍、實踐用途來做為出定義的改變，但這之中仍保持著『單元』、『流程』、『資料』；因此本專案將針對控制、資料面進行細部規劃。

## § Introduction

架構是一種概念，因此從文獻探討中可以知道 Dataflow 架構應從 Pipes & Filters 為基礎發展，並從而延伸成 [Progress 與 Layers](./doc/progress_vs_layers) 兩架構概念，而 Progress 運用於前端設計，Layers 則運用於後端設計；若以此為概念基礎，並以 Design Pattern 實踐 Pipes & Filters 的軟體設計方式。
> 需注意，即使能以 Design Pattern 來實踐了 Pipes & Filters、Layers，但這樣的設計未必不符合最後的應用需要，主要是考量分散技術的延伸應用，這些架構基礎都會依據對應框架而改變，但仍須注意其架構的概念與演變，從而找出適當的銜接標準。

+ Pipes
    - Decorator Pattern
    - Template method Pattern

+ Filters
    - Composite Pattern
    - Strategy Pattern

+ Store
    - Facade Pattern

+ Pipes & Filters application
    - Singleton Pattern
        - Facade Pattern
    - Flyweight Pattern
        - Command Pattern
    - Chain of Responsibility Pattern
    - Vistor Pattern

## § Library

## § Project command
