import { Component, OnInit } from '@angular/core';
import { PoemaService } from 'src/app/service/poema.service';

@Component({
  selector: 'app-cards',
  templateUrl: './cards.component.html',
  styleUrls: ['./cards.component.css']
})
export class CardsComponent implements OnInit {
  arrayPoemas: any[] = [];
  
  constructor(private poemaService: PoemaService,) { }
  
  ngOnInit(): void {
    
    this.poemaService.getPoemas().subscribe((data:any) =>{
      console.log('JSON data:', data.poemas);
      this.arrayPoemas = data.poemas})
     
    }
}
