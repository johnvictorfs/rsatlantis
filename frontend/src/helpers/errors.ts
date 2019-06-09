export function formatError(error: any) {
  let errorMessage: any = 'Erro inesperado :('
  if (error.response !== undefined) {
    errorMessage = Object.values(error.response.data)[0]
  } else {
    errorMessage = error.toString()
  }
  if (errorMessage === 'Error: Network Error') {
    return 'Erro: Falha de Conexão'
  }
  return errorMessage
}
