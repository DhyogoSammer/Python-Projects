<<<<<<< HEAD
class Heroi {
    constructor(nomeHeroi, idadeHeroi, classeHeroi) {
      this.nomeHeroi = nomeHeroi;
      this.idadeHeroi = idadeHeroi;
      this.classeHeroi = classeHeroi;
    }
  
    atacar() {
      let ataque;
  
      switch (this.classeHeroi) {
        case 'mago':
          ataque = 'usou magia';
          break;
        case 'guerreiro':
          ataque = 'usou espada';
          break;
        case 'monge':
          ataque = 'usou artes marciais';
          break;
        case 'ninja':
          ataque = 'usou shuriken';
          break;
        
      }
  
      console.log(`O ${this.classeHeroi} atacou usando ${ataque}`);
    }
  }
  
  // Exemplos de uso da classe
  const heroiGuerreiro = new Heroi('Hércules', 25, 'guerreiro');
  heroiGuerreiro.atacar();
  
  const heroiMago = new Heroi('Magnus', 70, 'mago');
  heroiMago.atacar();
  
  const heroiMonge = new Heroi('Shaolin', 63, 'monge');
  heroiMonge.atacar();

  const heroiNinja = new Heroi('Naruto', 18, 'ninja');
=======
class Heroi {
    constructor(nomeHeroi, idadeHeroi, classeHeroi) {
      this.nomeHeroi = nomeHeroi;
      this.idadeHeroi = idadeHeroi;
      this.classeHeroi = classeHeroi;
    }
  
    atacar() {
      let ataque;
  
      switch (this.classeHeroi) {
        case 'mago':
          ataque = 'usou magia';
          break;
        case 'guerreiro':
          ataque = 'usou espada';
          break;
        case 'monge':
          ataque = 'usou artes marciais';
          break;
        case 'ninja':
          ataque = 'usou shuriken';
          break;
        
      }
  
      console.log(`O ${this.classeHeroi} atacou usando ${ataque}`);
    }
  }
  
  // Exemplos de uso da classe
  const heroiGuerreiro = new Heroi('Hércules', 25, 'guerreiro');
  heroiGuerreiro.atacar();
  
  const heroiMago = new Heroi('Magnus', 70, 'mago');
  heroiMago.atacar();
  
  const heroiMonge = new Heroi('Shaolin', 63, 'monge');
  heroiMonge.atacar();

  const heroiNinja = new Heroi('Naruto', 18, 'ninja');
>>>>>>> ede9205a35862f059efceef86a268a148cc03dec
  heroiNinja.atacar();