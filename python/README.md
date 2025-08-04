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

<details><summary><h5>Sequence Diagram</h5></summary>

```mermaid
sequenceDiagram
    participant Main/Client

    create participant Logger
    Main/Client->>Logger: <<create>>

    create participant InfoHandler
    Logger->>InfoHandler: <<create>>
    create participant ErrorHandler
    Logger->>ErrorHandler: <<create>>
    create participant FailureHandler
    Logger->>FailureHandler: <<create>>

    Logger->>+InfoHandler: set_next(ErrorHandler)
    InfoHandler-->>-Logger: ErrorHandler
    Logger->>+ErrorHandler: set_next(FailureHandler)
    ErrorHandler-->>-Logger: FailureHandler

    Main/Client->>Logger: log()
    Logger->>+InfoHandler: handle()
    InfoHandler->>+ErrorHandler: handle()
    ErrorHandler->>+FailureHandler: handle()
    FailureHandler-->>-ErrorHandler: 
    ErrorHandler-->>-InfoHandler: 
    InfoHandler-->>-Logger: 
    Note left of Main/Client: This is in the case of <br> a request going to the last handler. <br><br> If the request have a certain criteria <br> that is handled by the an intermediate handler, <br> then the following handler will not be called <br> and the request will be returned to the first handler.
```
</details>

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
    
    InsertCommand o-- Editor : contains
    DeleteCommand o-- Editor : contains
    

    DeleteCommand --o Document : has
    InsertCommand --o Document : has

    namespace Commands{
        class InsertCommand
        class DeleteCommand
    }

    style Editor stroke:#4D85E6,stroke-width:3px
```

<details><summary><h5>Sequence Diagram</h5></summary>

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
</details>

## Iterator
#### What
We have a collection of items in a certain structure (item in list/graph, words in sentence ...). We want to traverse that collection. We split the storing and the traversal behaviour

#### Useful for
- Decouple the Client and the logic : The client doesn't need to know *how* or *what* to traverse, they just get the next item
- Having multiple Iterator for a type of collection (exemple: graph => depth or breadth traversal) 
- Simplify the collection : Only store and create the iterator for the kind of traversing we want


#### Exemple 
- `Iterator` : Interface that dictate the `next` method (traverse the collection)
- `IterableCollection` : Interface that dictate the `iter` method (give the mean to traverse the collection)
- `WordCollection` : Store the data and give access to an iterator
- `WordIterator` : Store the collection and the function to traverse it

```mermaid
classDiagram
    direction LR

    class Iterator {
        <<interface>>
        +__next__()* 
    }

    class IterableCollection {
        <<interface>>
        +__iter__()* 
    }

    class WordIterator {
        -words_collection list~str~
        -index int
        +__next__() str
    }

    class WordCollection {
        -words_collection list~str~
        +__len__() int
        +__getitem__(index: int) str
        +__iter__() WordIterator
        +get_reversed_iterator() WordIterator
    }
    
    Iterator <|.. WordIterator 
    IterableCollection <|.. WordCollection 

    WordIterator <|-- WordCollection 
    WordIterator --o WordCollection

    WordIterator <|-- Client 
    Client --|> WordCollection 

    style Client stroke:#4D85E6,stroke-width:3px
```

<details><summary><h5>Sequence Diagram</h5></summary>

```mermaid
sequenceDiagram
    participant Main/Client

    create participant WordCollection
    Main/Client->>WordCollection: <<create>>

    % --------------------------------------------------------
    rect rgba(61, 61, 61, 0.5)
        Main/Client->>WordCollection: __iter__()
        create participant WordIterator 
        WordCollection->>WordIterator: <<create>>
        WordCollection-->>Main/Client: return WordIterator

        loop Until End
            Main/Client->>+WordIterator: __next__()
            WordIterator-->>-Main/Client: 
        end
    end
    
    % --------------------------------------------------------
    rect rgba(61, 61, 61, 0.5)
        Main/Client->>WordCollection: get_reversed_iterator()
        create participant WordIteratorReversed 
        WordCollection->>WordIteratorReversed: <<create>>
        WordCollection-->>Main/Client: return WordIteratorReversed

        loop Until End
            Main/Client->>+WordIteratorReversed: __next__()
            WordIteratorReversed-->>-Main/Client: 
        end
    end
```
</details>


## Mediator

Not really useful

Just set a class that let you interface with a certain set of other object (exemple: A Dialog let us talk to its child (button, menus ...))

## Memento
#### What
A class that store/remember an object state. 

#### Useful for
Some undo redo operation, transactional operations, rollbacks, versioning ...

#### Exemple
- `Memento` : Interface that dictate the `get_save` method
- `Originator` : Interface that dictate the `save` method
- `TextEditor` : Store the current text state
- `TextEditorSnapshot` : Store **a** text state at a certain time. Do not expose the internal state
- `History` : Store the collection of `TextEditorSnapshot`. Have no access to its internal state

```mermaid
classDiagram
    direction LR

    class Memento {
        <<interface>>
        +get_save()* 
    }

    class Originator {
        <<interface>>
        +save()* 
    }

    class TextEditorSnapshot {
        -state str
        +get_save() str
    }

    class TextEditor {
        -state str
        +write(text: str)
        +save() TextEditorSnapshot
        +restore(snapshot: TextEditorSnapshot)
        +display()
    }

    class History {
        -mementos list~TextEditorSnapshot~
        -originator TextEditor
        +backup()
        +undo()
    }

    class Client {
        +editor TextEditor
        +history History
    }

    Memento <|.. TextEditorSnapshot
    Originator <|.. TextEditor

    TextEditorSnapshot *-- History
    TextEditor *-- History

    History <|-- Client
    TextEditor <|-- Client

    style Client stroke:#4D85E6,stroke-width:3px
```

<details><summary><h5>Sequence Diagram</h5></summary>

```mermaid
sequenceDiagram
    participant Client

    create participant TextEditor
    Client->>TextEditor: <<create>>
    
    rect rgba(61, 61, 61, 0.5)
        create participant History
        Client->>+History: <<create>>
        Client->>History: __init__(TextEditor)
        History-->>-Client: 
    end

    % --------------------------------------------------------
    Client->>+TextEditor: write()
    TextEditor-->>-Client: 

    rect rgba(61, 61, 61, 0.5)
        Client->>History: backup()
        History->>+TextEditor: save()
        
        rect rgba(61, 61, 61, 0.7)
            create participant TextEditorSnapshot
            TextEditor->>+TextEditorSnapshot: <<create>>
            TextEditor->>TextEditorSnapshot: __init__(state)
            TextEditorSnapshot-->>-TextEditor: 
        end
        
        TextEditor-->>-History: Store snapshot
    end

    
    % --------------------------------------------------------
    rect rgba(61, 61, 61, 0.5)
        Client->>History: undo()
        History->>+TextEditor: restore(TextEditorSnapshot)
        TextEditor->>+TextEditorSnapshot: get_save()
        TextEditorSnapshot-->>-TextEditor: restore state
        TextEditor-->>-Client: 

    end
```

</details>




## Observer
#### What
Observer pattern can subscribe to other objects and receive notification

#### Useful for 
- Send info to different system without them checkin continuously
- We can dynamically attach or detach observers at runtime
- Decouple the publisher from the action took (Here we send log info, but we don't know how is it handled)

#### Exemple
- `Subscriber` : dictate the `update` function
- `ConsoleSubscriber`, `FileSubscriber` : manage the reception of a message and handle how to proccess it (or pass it to the right system)
- `LoggerPublisher` : Emit the event to the Subscriber it have


```mermaid
classDiagram
    direction LR

    class Subscriber {
        <<interface>>
        +update(context)* 
    }

    class ConsoleSubscriber {
        +update(message:str, level:str)
    }

    class FileSubscriber {
        +filename str
        +update(message:str, level:str)
    }

    class LoggerPublisher {
        -_observers list~Subscriber~
        +attach(observer:Subscriber)
        +detach(observer:Subscriber)
        +log(message:str, level:str)
        -notify(message:str, level:str)
    }

    class Client {
        +logger LoggerPublisher
        +console_handler ConsoleSubscriber
        +file_subscriber FileSubcriber
    }


    Subscriber <|.. ConsoleSubscriber
    Subscriber <|.. FileSubscriber

    ConsoleSubscriber <--* LoggerPublisher
    FileSubscriber <--* LoggerPublisher

    LoggerPublisher <-- Client
    FileSubscriber <-- Client
    ConsoleSubscriber <-- Client

    style Client stroke:#4D85E6,stroke-width:3px

```

<details><summary><h5>Sequence Diagram</h5></summary>

```mermaid
sequenceDiagram
    participant Client

    create participant LoggerPublisher
    Client->>LoggerPublisher: <<create>>

    create participant ConsoleSubscriber
    Client->>ConsoleSubscriber: <<create>>
    
    rect rgba(61, 61, 61, 0.5)
        create participant FileSubscriber
        Client->>+FileSubscriber: <<create>>
        Client->>FileSubscriber: __init__("app.log")
    end

    % --------------------------------------------------------
    Client->>+LoggerPublisher: attach(console_subscriber)
    LoggerPublisher-->-Client: 
    Client->>+LoggerPublisher: attach(file_subscriber)
    LoggerPublisher-->-Client: 

    Client->>+LoggerPublisher: log()
    LoggerPublisher->>LoggerPublisher: _notify()
    activate LoggerPublisher
    LoggerPublisher->>+ConsoleSubscriber: update()
    ConsoleSubscriber-->-LoggerPublisher: 
    LoggerPublisher->>+FileSubscriber: update()
    FileSubscriber-->-LoggerPublisher: 
    deactivate LoggerPublisher
    LoggerPublisher-->-Client: 

```
</details>


## State
#### What
Extracting the state of an object into a separate set of class. Each class contains the logic and can change dynamically the state of the context object to another state if wanted.

#### Useful for
- Managing a state system and avoiding bloat/mess with an accumulation of conditions

#### Exemple





```mermaid
classDiagram
    direction LR

    class State {
        <<abstract>>
        -player:AudioPlayer
        +State(audio_player:AudioPlayer)
        +set_player(audio_player:AudioPlayer) 
        +on_play()*
        +on_pause()*
        +on_stop()*
    }

    class StoppedState {
        +on_play()
        +on_pause()
        +on_stop()
    }
    
    class PlayingState {
        +on_play()
        +on_pause()
        +on_stop()
    }   

    class PausedState {
        +on_play()
        +on_pause()
        +on_stop()
    }

    class AudioPlayer {
        -state:State
        +AudioPlayer(initial_state:State)
        +change_state(new_state:State)
        +click_play()
        +click_pause()
        +click_stop()
    }


    State <|..StoppedState
    State <|..PlayingState
    State <|..PausedState
    AudioPlayer o--|> State

    style AudioPlayer stroke:#4D85E6,stroke-width:3px
```

<details><summary><h5>Sequence Diagram</h5></summary>

```mermaid

sequenceDiagram
    participant Client

    create participant StoppedState
    Client->>StoppedState: <<create>>

    rect rgba(61, 61, 61, 0.5)
        create participant AudioPlayer
        Client->>+AudioPlayer: <<create>>
        Client->>AudioPlayer: AudioPlayer(initial_state)
        AudioPlayer->>StoppedState: set_player(self)
    end

    % --------------------------------------------------------
    rect rgba(61, 61, 61, 0.5)
        Client->>AudioPlayer: click_play()
        AudioPlayer->>StoppedState: on_play()

        rect rgba(61, 61, 61, 0.5)
            create participant PlayingState
            StoppedState->>PlayingState: <<create>>
            StoppedState->>PlayingState: PlayingState(self.player)
        end

        StoppedState->>AudioPlayer: change_state(PlayingState)
    end

    % --------------------------------------------------------
    rect rgba(61, 61, 61, 0.5)
        Client->>AudioPlayer: click_play()
        AudioPlayer->>PlayingState: on_play()
        PlayingState-->>AudioPlayer: print("Already playing.")
    end
```

</details>


## Strategy
#### What
A way to externalize algorithm from an object.

It architecture is similar to `State` but it does not externalize state but logic.

It looks similar to `Command` because it parameterizes an object with action. But `Command` convert an operation in an object, while `Strategy` describes different way of doing the same thing, letting us swap algorithms in a signle *context* class

#### Useful For
- Simplifying the `Context` class by externalizing the logic.
- We can easily add other algorithms without touching the `Context` class.
- We can change the algorithm at runtime.

#### Example


```mermaid
classDiagram
    direction LR

    class ExportStrategy {
        <<interface>>
        +export(canvas: ImageCanvas)
    }

    class PngExportStrategy {
        +export(Canvas canvas)
    }
    class JpegExportStrategy {
        +export(Canvas canvas)
    }
    class SvgExportStrategy {
        +export(Canvas canvas)
    }

    class ImageCanvas {
        -shapes: list[]
        +add_shape(shape_data)
    }

    class ImageExporter {
        -strategy: ExportStrategy
        +set_strategy(strategy: ExportStrategy)
        +do_export(canvas: ImageCanvas, filepath: str)
    }

    ExportStrategy <|.. PngExportStrategy
    ExportStrategy <|.. JpegExportStrategy
    ExportStrategy <|.. SvgExportStrategy

    ImageExporter --> ExportStrategy
    ImageExporter o-- ExportStrategy

    ExportStrategy <|-- Client
    ImageExporter <|-- Client
    Client --|> ImageCanvas

    style Client stroke:#4D85E6,stroke-width:3px

```

<details><summary><h5>Sequence Diagram</h5></summary>

```mermaid
sequenceDiagram
    participant Client

    create participant ImageCanvas
    Client->>ImageCanvas: <<create>>
    Client->>ImageCanvas: add_shape("circle")

    create participant PngExportStrategy
    Client->>PngExportStrategy: <<create>>

    rect rgba(61, 61, 61, 0.5)
        create participant ImageExporter
        Client->>ImageExporter: <<create>>
        Client->>ImageExporter: ImageExporter(PngExportStrategy())
    end


    % --------------------------------------------------------
    
    rect rgba(61, 61, 61, 0.5)
        Client->>ImageExporter: do_export(my_canvas, "my_drawing.png")
        ImageExporter->>PngExportStrategy: export(canvas, filepath)
    end

    % --------------------------------------------------------
    rect rgba(61, 61, 61, 0.5)
        create participant JpegExportStrategy
        Client->>JpegExportStrategy: <<create>>
        Client->>ImageExporter: set_strategy(JpegExportStrategy())
    end

    rect rgba(61, 61, 61, 0.5)
        Client->>ImageExporter: do_export(my_canvas, "my_drawing.png")
        ImageExporter->>JpegExportStrategy: export(canvas, filepath)
    end


```

</details>







# Creational


# Structural