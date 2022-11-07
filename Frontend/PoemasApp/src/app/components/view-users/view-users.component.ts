import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UsuarioService } from './../../service/usuario.service';
@Component({
  selector: 'app-view-users',
  templateUrl: './view-users.component.html',
  styleUrls: ['./view-users.component.css']
})
export class ViewUsersComponent implements OnInit {
    
    arrayUsuarios: any[] = [];

    constructor(
      //private router: Router,
      private postUsuario: UsuarioService,
    ) { } 
  

  ngOnInit(): void {
    
    this.postUsuario.getUsuarios().subscribe((data:any) =>{
      console.log('JSON data:', data.usuarios);
      this.arrayUsuarios = data.usuarios})
     
    }
  }

