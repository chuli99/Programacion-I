import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ModalPoemasComponent } from './modal-poemas.component';

describe('ModalPoemasComponent', () => {
  let component: ModalPoemasComponent;
  let fixture: ComponentFixture<ModalPoemasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ModalPoemasComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ModalPoemasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
