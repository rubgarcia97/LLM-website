class Prompt:
    
    def __init__(self) -> None:
        pass

    def prompt(self,imput1=None,imput2=None,imput3=None,imput4=None):

        concat0 = "Estoy pensando en hacer alguna receta saludable,"
        concat1 = ""
        concat2 = ""
        concat3 = ""
        concat4 = ""

        if imput1 is not None:
            concat1 = f"La idea es hacerla para {imput1}."

        if imput2 is not None:
            concat2 = f"es fundamental que contenga: {imput2}."

        if imput3 is not None:
            concat3 = f"ademas, tiene que tener un aporte calórico aproximado de {imput3} kcal."

        if imput4 is not None:
            concat4 = f"Es importante que prioricemos {imput4}."


        return concat0+concat1+concat2+concat3+concat4

