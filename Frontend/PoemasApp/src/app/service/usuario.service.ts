import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})

export class UsuarioService {
  url = 'api/usuarios';
  
  constructor(
  private httpClient: HttpClient
  ) { } 
  getUsuarios() {
    return this.httpClient.get(this.url);
  } 
  //getUsuario()
}


