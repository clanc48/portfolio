<?php
use Illuminate\Support\Facades\Artisan;
Artisan::command('demo:status', function () { $this->info('Hale Mercer demo ready.'); });
