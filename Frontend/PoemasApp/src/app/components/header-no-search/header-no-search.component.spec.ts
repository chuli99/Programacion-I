import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HeaderNoSearchComponent } from './header-no-search.component';

describe('HeaderNoSearchComponent', () => {
  let component: HeaderNoSearchComponent;
  let fixture: ComponentFixture<HeaderNoSearchComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HeaderNoSearchComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HeaderNoSearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
