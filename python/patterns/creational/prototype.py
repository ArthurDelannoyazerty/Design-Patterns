import copy

class Button:
    def __init__(self, text: str, styles: list):
        self.text = text
        self.styles = styles

    def __str__(self):
        return (
            f"Button(ID: {id(self)}, Text: '{self.text}', "
            f"Styles: {self.styles} at ID: {id(self.styles)})"
        )

    def __copy__(self):
        return self.__class__(self.text, self.styles)

    def __deepcopy__(self, memo):
        result = self.__class__.__new__(self.__class__)
        
        # Add the new instance to the memo dict *before* copying attributes
        # to handle self-referential objects.
        memo[id(self)] = result
        
        # Copy the attributes, passing the memo dict along
        result.text = copy.deepcopy(self.text, memo)
        result.styles = copy.deepcopy(self.styles, memo)
        
        return result

# ---------------------------------------------------------------------------- #
#                                  Main/Client                                 #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":

    primary_styles = ["btn", "btn-primary", "font-bold"]
    prototype_button = Button(text="Submit", styles=primary_styles)

    print("--- SHALLOW Copy (copy.copy) ---")
    
    # Use the prototype to create a new button
    cancel_button_shallow = copy.copy(prototype_button)

    #Modify the internal copied object state
    cancel_button_shallow.text = "Cancel" 
    cancel_button_shallow.styles.append("btn-warning") 

    print("\nAfter shallow copy modification:")
    print(f"  Original:     {prototype_button}")
    print(f"  Shallow Copy: {cancel_button_shallow}")
    print("\nConclusion: Because the list was only referenced (not copied), modifying it in the clone also modified it in the original prototype.")
    
    # 3. Reset the prototype to its original state for a fair comparison
    prototype_button.styles.pop() # Remove the 'btn-warning' style

    print("\n--- DEEP Copy (copy.deepcopy) ---")

    # Use the prototype to create another new button
    cancel_button_deep = copy.deepcopy(prototype_button)

    #Modify the internal copied object state
    cancel_button_deep.text = "Cancel" 
    cancel_button_deep.styles.append("btn-warning") 

    print("\nAfter deep copy modification:")
    print(f"  Original:  {prototype_button}")
    print(f"  Deep Copy: {cancel_button_deep}")
    print("\nConclusion: The deep copy is a new object, and its states are  ALSO NEW, SEPARATE OBJECTS in memory.")

# ---------------------------------- Output ---------------------------------- #

# --- SHALLOW Copy (copy.copy) ---
#
# After shallow copy modification:
#   Original:     Button(ID: 1273975193552, Text: 'Submit', Styles: ['btn', 'btn-primary', 'font-bold', 'btn-warning'] at ID: 1273975352320)
#   Shallow Copy: Button(ID: 1273975192736, Text: 'Cancel', Styles: ['btn', 'btn-primary', 'font-bold', 'btn-warning'] at ID: 1273975352320)
#
# Conclusion: Because the list was only referenced (not copied), modifying it in the clone also modified it in the original prototype.
#
# --- DEEP Copy (copy.deepcopy) ---
#
# After deep copy modification:
#   Original:  Button(ID: 1273975193552, Text: 'Submit', Styles: ['btn', 'btn-primary', 'font-bold'] at ID: 1273975352320)     
#   Deep Copy: Button(ID: 1273975191104, Text: 'Cancel', Styles: ['btn', 'btn-primary', 'font-bold', 'btn-warning'] at ID: 1273975352128)
#
# Conclusion: The deep copy is a new object, and its states are  ALSO NEW, SEPARATE OBJECTS in memory.
