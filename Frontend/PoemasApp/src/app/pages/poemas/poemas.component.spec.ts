import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PoemasComponent } from './poemas.component';

describe('PoemasComponent', () => {
  let component: PoemasComponent;
  let fixture: ComponentFixture<PoemasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PoemasComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PoemasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
