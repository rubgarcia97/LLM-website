import dash
from dash import dcc, html, Input, Output, State
from llm_chat import Chat

app = dash.Dash(__name__)

# Diseño de la aplicación
app.layout = html.Div([
    dcc.Input(id='input-1', type='text', value=''),
    dcc.Input(id='input-2', type='text', value=''),
    html.Button('Guardar', id='button'),
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
        chat_content = Chat().request(input_1=variable_1, input_2=variable_2)
        
        # Devolver el contenido de chat dentro de un componente html.Div
        return html.Div(chat_content)

if __name__ == '__main__':
    app.run_server(debug=True)
