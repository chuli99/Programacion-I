import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { LoginComponent } from './pages/login/login.component';
import { PoemasComponent } from './pages/poemas/poemas.component';
import { DashboardAdminComponent } from './pages/dashboard-admin/dashboard-admin.component'
import { DashboardUserComponent } from './pages/dashboard-user/dashboard-user.component'

const routes: Routes = [
  {path:'',component:HomeComponent},
  {path:'login',component:LoginComponent},
  {path:'poemas',component:PoemasComponent},
  {path:'admin',component:DashboardAdminComponent},
  {path:'user',component:DashboardUserComponent},
  {path: 'user/:id', component:DashboardUserComponent },
  {path:'poema/:id',component:PoemasComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
