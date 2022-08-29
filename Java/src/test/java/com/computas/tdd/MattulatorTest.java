package com.computas.tdd;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/**
 * Enhetstester for <code>Mattulator</code>.
 */
public class MattulatorTest {
	/**
	 * Sjekk at når vi plusser en og to så får vi tre.
	 */
	@Test
	public void enPlussToErTre() {
		// Arrange: få en mattulator instansiert slik at vi er klare til å teste
		// funksjonalitet
		Mattulator mattulator = new Mattulator();

		// Act: vi plusser...
		double actual = mattulator.adder(1D, 2D);

		// Assert: ...og sjekker at resultatet ble riktig
		assertEquals(3D, actual);
	}
}
