const CREDENCIAIS_CORRETAS = {
  usuario: 'admin',
  senhaHash: 'e35e97f6905c64bd921de63e1ef45c64' 
};

function calcularHashSenhaMD5(senha) {
  return md5(senha); // Calcula o hash MD5 da senha
}

function login() {
  const senhaInserida = document.getElementById('password').value;

  // Calcula a hash MD5 da senha inserida no HTML
  const senhaHashInserida = calcularHashSenhaMD5(senhaInserida);

  // Verifica se a hash da senha inserida corresponde à hash armazenada no código
  if (senhaHashInserida === CREDENCIAIS_CORRETAS.senhaHash) {
    window.location.href = '../Desktop/index.html';;
  } else {
    alert('Credenciais incorretas. Tente novamente.');
  }
}

