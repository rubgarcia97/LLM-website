import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State
from llm_chat import Chat
from prompt import Prompt

external_css = ["/assets/style.css"]
app = dash.Dash(__name__,external_stylesheets=external_css)

server = app.server

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
                        dbc.ModalBody([
                            html.Div(id='text-modal',children='vamoh a jugar')
                        ]),
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
    Output('text-modal', 'children'),
    [
        Input('open-body-scroll', 'n_clicks'),
        Input('close-body-scroll', 'n_clicks'),
    ],
    [
        State('input-1', 'value'),
        State('input-2', 'value'),
        State('input-3', 'value'),
        State('input-4', 'value'),
        State('modal-body-scroll', 'is_open'),
        State('text-modal', 'children')
    ]
)
def update_output(n_clicks_open, n_clicks_close, input1, input2, input3, input4, is_open, children):
    if n_clicks_open or n_clicks_close:
        # Procesa los valores de entrada
        children = Chat().request(input_1=input1, input_2=input2, input_3=input3, input_4=input4)
        return not is_open, children  # Devuelve ambos valores
    return is_open, children  # Devuelve los valores actuales si no se hace clic

    

if __name__ == '__main__':
    app.run(debug=True)
