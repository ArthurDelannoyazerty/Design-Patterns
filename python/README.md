# Behavioral
## Chain of Responsibility

#### What
Pass a request through a chain of handlers. Each handler decides whether to process the request or pass it to the next handler in the chain.

#### Useful for
- avoiding coupling between objects. The sender only need to know *how* to send the request, not *who* will handle it
- Adding/removing handlers easily (isolated codes)
- Single Responsibility Principle

#### Exemple

BASE
- `Handler` : Interface that dictate what methods are mandatory
- `AbstractHandler` : Boilerplate code for the handlers

EXAMPLE
- `InfoHandler`, `ErrorHandler`, `FailureHandler` : Concrete handlers that each implement a way of processing the request
- `Logger` : Controller that build the chain of handlers and send the request to the first handler. Help use the chain of responsibility 

```mermaid
---
config:
    theme: 'base'
    themeVariables:
       background: '#727272ff'
---
classDiagram
    direction LR

    class Handler {
        <<interface>>
        +set_next(handler: Handler) Handler
        +handle(request) Optional~str~
    }

    class AbstractHandler {
        <<abstract>>
        -Handler _next_handler
        +set_next(handler: Handler) Handler
        +handle(request: str) Optional~str~
    }

    class InfoHandler {
        +handle(request: str) Optional~str~
    }
    class ErrorHandler {
        +handle(request: str) Optional~str~
    }
    class FailureHandler {
        +handle(request: str) Optional~str~
    }

    class Logger {
        -Handler default_handler
        +log(message: str) None
    }

    Handler <|-- AbstractHandler : implements
    
    AbstractHandler <|-- InfoHandler
    AbstractHandler <|-- ErrorHandler : implements
    AbstractHandler <|-- FailureHandler

    InfoHandler    o-- Logger
    ErrorHandler   o-- Logger : Uses
    FailureHandler o-- Logger

    namespace Handlers {
        class InfoHandler
        class ErrorHandler
        class FailureHandler
    }
```

```mermaid
sequenceDiagram
    Logger->>+InfoHandler: request
    InfoHandler->>+ErrorHandler: request
    ErrorHandler->>+FailureHandler: request
    FailureHandler-->>-ErrorHandler: None | Any
    ErrorHandler-->>-InfoHandler: None | Any
    InfoHandler-->>-Logger: None | Any
    Note left of Logger: This is in the case of <br> a request going to the last handler. <br><br> If the request have a certain criteria <br> that is handled by the an intermediate handler, <br> then the following handler will not be called <br> and the request will be returned to the first handler.
```


# Creational


# Structural