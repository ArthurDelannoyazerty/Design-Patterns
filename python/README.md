# Behavioral
## Chain of Responsibility
#### What
Pass a request through a chain of handlers. Each handler decides whether to process the request or pass it to the next handler in the chain.

#### Useful for
- Avoiding coupling between objects. The sender only need to know *how* to send the request, not *who* will handle it
- Adding/removing handlers is easy (code isolation)
- Single Responsibility Principle

#### Exemple
- `Handler` : Interface that dictate what methods are mandatory
- `AbstractHandler` : Boilerplate code for the handlers
- `InfoHandler`, `ErrorHandler`, `FailureHandler` : Concrete handlers that each implement a way of processing the request
- `Client` | `Logger` : Controller that build the chain of handlers and send the request to the first handler. Help use the chain of responsibility 

```mermaid
classDiagram
    direction LR

    class Handler {
        <<interface>>
        +set_next(handler: Handler)* Handler
        +handle(request)* Optional~str~
    }

    class AbstractHandler {
        <<abstract>>
        -Handler _next_handler
        +set_next(handler: Handler) Handler
        +handle(request: str)* Optional~str~
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

    Handler <|.. AbstractHandler : implements
    
    AbstractHandler <|-- InfoHandler
    AbstractHandler <|-- ErrorHandler : extends
    AbstractHandler <|-- FailureHandler

    InfoHandler    o-- Logger
    ErrorHandler   o-- Logger : Uses
    FailureHandler o-- Logger

    namespace Handlers {
        class InfoHandler
        class ErrorHandler
        class FailureHandler
    }

    style Logger stroke:#4D85E6,stroke-width:3px
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


## Command
#### What
Encapsulate all the information needed to perform an action. Each command can do an action or delegate it to a receiver. An invoker will execute these commands.

#### Useful for
- Decoupling the sender and receiver of a request (the invoker don't need to know the receiver implementation, it just execute the command)
- Adding/removing commands is easy (code isolation)
- Creating command history with undo/redo operations

#### Exemple
- `Command` : Interface that dictate the `execute` and `undo` method
- `Receiver` | `Document` : Contains the complex/external business logic
- `InsertCommand`, `DeleteCommand` : Implement the `execute` and `undo` method 
- `Invoker` | `Editor` : Contains the commands and execute them

```mermaid
classDiagram
    direction LR
    class Command {
        <<interface>>
        +execute()*
        +undo()*
    }

    class InsertCommand {
        -document: Document
        -text : str
        +execute()
        +undo()
    }

    class DeleteCommand {
        -document: Document
        -length : int
        -deleted_text : str
        +execute()
        +undo()
    }

    class Document {
        +text
        +cursor_pos
        +insert(text: str)
        +delete(length: int)
    }

    class Editor {
        -document: Document
        -history: list[Command]
        +type(text: str)
        +backspace(length: int)
        -execute_command(command: Command)
        +undo()
    }
    

    Command <|.. InsertCommand : implements
    Command <|.. DeleteCommand : implements
    
    InsertCommand o-- Editor : has
    DeleteCommand o-- Editor : has
    

    DeleteCommand --o Document : has
    InsertCommand --o Document : has

    namespace Commands{
        class InsertCommand
        class DeleteCommand
    }

    style Editor stroke:#4D85E6,stroke-width:3px
```

```mermaid
sequenceDiagram
    participant Main/Client

    create participant Editor
    Main/Client->>Editor: <<create>>

    create participant Document
    Editor->>Document: <<create>>
    
    % --------------------------------------------------------
    rect rgba(61, 61, 61, 0.5)
    Main/Client->>+Editor: type("Hello, this is the Command Pattern.")

    create participant InsertCommand1 as InsertCommand
    Editor->>InsertCommand1: <<create>>

    Editor->>+Editor: execute_command()
    Editor->>+InsertCommand1: execute()
    InsertCommand1->>+Document: insert()
    Document-->>-InsertCommand1: 
    InsertCommand1-->>-Editor: 
    Editor->>-Editor: Add command to history
    Editor-->>-Main/Client:
    end

    % --------------------------------------------------------
    rect rgba(61, 61, 61, 0.5)
    Main/Client->>+Editor: type(" It's great!")

    create participant InsertCommand2 as InsertCommand
    Editor->>InsertCommand2: <<create>>

    Editor->>+Editor: execute_command()
    Editor->>+InsertCommand2: execute()
    InsertCommand2->>+Document: insert()
    Document-->>-InsertCommand2: 
    InsertCommand2-->>-Editor: 
    Editor->>-Editor: Add command to history
    Editor-->>-Main/Client:
    end

    % --------------------------------------------------------
    rect rgba(61, 61, 61, 0.5)
    Main/Client->>+Editor: backspace(7)

    create participant DeleteCommand1 as DeleteCommand
    Editor->>DeleteCommand1: <<create>>

    Editor->>+Editor: execute_command()
    Editor->>+DeleteCommand1: execute()
    DeleteCommand1->>+Document: delete(self.length)
    Document-->>-DeleteCommand1: 
    DeleteCommand1-->>-Editor: 
    Editor->>-Editor: Add command to history
    Editor-->>-Main/Client:
    end

    % --------------------------------------------------------
    rect rgba(61, 61, 61, 0.5)
    Main/Client->>+Editor: undo()

    Editor->>+DeleteCommand1: undo()
    DeleteCommand1->>+Document: insert(self._deleted_text)
    Document-->>-DeleteCommand1: 
    DeleteCommand1-->>-Editor: 
    Editor-->>-Main/Client:
    end

    % --------------------------------------------------------
    box rgba(158, 158, 158, 0.17) Commands
        participant InsertCommand1
        participant InsertCommand2
        participant DeleteCommand1
    end
```

# Creational


# Structural