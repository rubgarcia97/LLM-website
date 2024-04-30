import dash
from dash import dcc, html, Input, Output, State
from llm_chat import Chat

app = dash.Dash(__name__)

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
                dcc.Input(id='input-1',placeholder="Tipo 1", type='text', value='', style={'width':'260px','position': 'absolute', 'left': '10%', 'top': '50%'})
            ]),
            html.Div([
                dcc.Input(id='input-2', type='text', value='', style={'width':'260px','position': 'absolute', 'left': '10%', 'top': '56%'})
            ]),
            html.Div([
                dcc.Input(id='input-3', type='text', value='', style={'width':'260px','position': 'absolute', 'left': '10%', 'top': '62%'})
            ]),
            html.Div([
                dcc.Input(id='input-4', type='text', value='', style={'width':'260px','position': 'absolute', 'left': '10%', 'top': '68%'})
            ]),
            html.Button('Generar Receta', id='button', style={'position': 'absolute', 'left': '37%', 'top': '91.2%','background-color': 'white','border':'None','box-shadow':'None','font-size':'16px'})
    ]),
        html.Div(id='output-container')  # Nuevo div para mostrar el contenido de chat
])

# Callback para manejar el evento de clic del botón y almacenar los valores de las cajas de texto
@app.callback(
    Output('output-container', 'children'),
    [Input('button', 'n_clicks')],
    [State('input-1', 'value'),
     State('input-2', 'value')]
)
def update_output(n_clicks, input1, input2):
    if n_clicks is not None:
        # Aquí puedes hacer lo que quieras con los valores de las cajas de texto
        # Por ejemplo, puedes almacenarlos en variables
        variable_1 = input1
        variable_2 = input2

        # Obtener el contenido de chat
        #chat_content = Chat().request(input_1=variable_1, input_2=variable_2)
        
        # Devolver el contenido de chat dentro de un componente html.Div
        return 0#html.Div(chat_content)

if __name__ == '__main__':
    app.run_server(debug=True, port=5000)
