import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PageNavigAdminComponent } from './page-navig-admin.component';

describe('PageNavigAdminComponent', () => {
  let component: PageNavigAdminComponent;
  let fixture: ComponentFixture<PageNavigAdminComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PageNavigAdminComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PageNavigAdminComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
