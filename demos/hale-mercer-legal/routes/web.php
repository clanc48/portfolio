<?php
use Illuminate\Support\Facades\Route;
Route::view('/', 'home')->name('home');
Route::view('/practice-areas', 'practice-areas')->name('practice-areas');
Route::view('/attorneys', 'attorneys')->name('attorneys');
Route::view('/insights', 'insights')->name('insights');
Route::view('/consultation', 'consultation')->name('consultation');
