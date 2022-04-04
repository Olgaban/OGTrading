import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InputComponent } from './input/input.component';
import { OutputComponent } from './output/output.component';

const routes: Routes = [
  {path: '', component: InputComponent},
  {path: 'sequence', component: OutputComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
