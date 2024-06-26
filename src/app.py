import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State
from llm_chat import Chat
from prompt import Prompt

external_css = ["/assets/style.css"]
app = dash.Dash(__name__,external_stylesheets=external_css)

# Diseño de la aplicación
app.layout = html.Div(style={
                'background-image':'url("/assets/main.png")',
                'height':'852px', 'width':'393px',
                #'height':'65%', 'width':'100%',
                'position':'absolute'
            },
    children=[
        html.Div([
            html.Div([
                dcc.Input(id='input-1',placeholder="Desayuno, Comida, Cena...", type='text', value='', style={'width':'260px','position': 'absolute', 'left': '10%', 'top': '50%'})
            ]),
            html.Div([
                dcc.Input(id='input-2',placeholder="Algún ingrediente concreto?", type='text', value='', style={'width':'260px','position': 'absolute', 'left': '10%', 'top': '56%'})
            ]),
            html.Div([
                dcc.Input(id='input-3',placeholder="Cuantas kcal aproximadamente?", type='text', value='', style={'width':'260px','position': 'absolute', 'left': '10%', 'top': '62%'})
            ]),
            html.Div([
                dcc.Input(id='input-4',placeholder="Priorizamos Proteínas, HC, Grasas, sabor...? ", type='text', value='', style={'width':'260px','position': 'absolute', 'left': '10%', 'top': '68%'})
            ]),
            html.Div([
                dbc.Button('Generar Receta', id='open-body-scroll',n_clicks=0, style={'position': 'absolute', 'left': '37%', 'top': '91.2%','background-color': 'white','border':'None','box-shadow':'None','font-size':'15px'}),
                dbc.Modal(
                    [
                        dbc.ModalHeader(dbc.ModalTitle("Generar Receta")),
                        dbc.ModalBody("Holi"),
                        dbc.ModalFooter(
                            dbc.Button(
                                "Cerrar",
                                id="close-body-scroll",
                                className="ms-auto",
                                n_clicks=0,
                            )
                        ),
                    ],
                    id='modal-body-scroll',
                    scrollable=True,
                    is_open=False,
                ),
            ]
        )
    ])
        #html.Div(id='output-container')  # Nuevo div para mostrar el contenido de chat
])

# Callback para manejar el evento de clic del botón y almacenar los valores de las cajas de texto
@app.callback(
    Output('modal-body-scroll', 'is_open'),
    [
        Input('open-body-scroll', 'n_clicks'),
        Input("close-body-scroll","n_clicks"),
    ],
    [State('input-1', 'value'),
     State('input-2', 'value'),
     State('input-3', 'value'),
     State('input-4', 'value'),
     State('modal-body-scroll','is_open')]
)
def update_output(n_clicks_open, n_clicks_close, input1, input2, input3, input4,is_open):
    if n_clicks_open or n_clicks_close:
        return not is_open
    return is_open
    """
    if n_clicks is not None:
        # Aquí puedes hacer lo que quieras con los valores de las cajas de texto
        # Por ejemplo, puedes almacenarlos en variables
        variable_1 = input1
        variable_2 = input2
        variable_3 = imput3
        variable_4 = imput4


        # Obtener el contenido de chat
        #chat_content = Chat().request(input_1=variable_1, input_2=variable_2)
        prompt = Prompt().prompt(imput1=variable_1,imput2=variable_2,imput3=variable_3,imput4=variable_4)
        # Devolver el contenido de chat dentro de un componente html.Div
        return html.Div(prompt)#html.Div(chat_content)
    """
    

if __name__ == '__main__':
    app.run_server(debug=True, port=5000)
