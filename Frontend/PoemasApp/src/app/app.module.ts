import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FooterComponent } from './components/footer/footer.component';
import { HomeComponent } from './pages/home/home.component';
import { CardsComponent } from './components/cards/cards.component';
import { LoginComponent } from './pages/login/login.component';
import { DashboardUserComponent } from './pages/dashboard-user/dashboard-user.component';
import { DashboardAdminComponent } from './pages/dashboard-admin/dashboard-admin.component';
import { PoemasComponent } from './pages/poemas/poemas.component';
import { DropdownComponent } from './components/dropdown/dropdown.component';
import { ModalComponent } from './components/modal-user/modal-user.component';
import { PageNavigHomeComponent } from './components/page-navig-home/page-navig-home.component';
import { ModalPoemasComponent } from './components/modal-poemas/modal-poemas.component';
import { PageNavigAdminComponent } from './components/page-navig-admin/page-navig-admin.component';
import { HeaderComponent } from './components/header/header.component';



@NgModule({
  declarations: [
    AppComponent,
    FooterComponent,
    HomeComponent,
    CardsComponent,
    LoginComponent,
    DashboardUserComponent,
    DashboardAdminComponent,
    PoemasComponent,
    DropdownComponent,
    ModalComponent,
    PageNavigHomeComponent,
    ModalPoemasComponent,
    PageNavigAdminComponent,
    HeaderComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
