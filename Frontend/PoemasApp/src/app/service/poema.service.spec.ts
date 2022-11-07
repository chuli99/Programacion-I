import { TestBed } from '@angular/core/testing';

import { PoemaService } from './poema.service';

describe('PoemaService', () => {
  let service: PoemaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PoemaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
