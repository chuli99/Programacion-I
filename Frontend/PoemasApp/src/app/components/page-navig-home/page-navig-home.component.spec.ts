import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PageNavigHomeComponent } from './page-navig-home.component';

describe('PageNavigHomeComponent', () => {
  let component: PageNavigHomeComponent;
  let fixture: ComponentFixture<PageNavigHomeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PageNavigHomeComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PageNavigHomeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
