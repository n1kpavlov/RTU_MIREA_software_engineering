package ru.mirea.asu.config;

import com.google.zxing.BarcodeFormat;
import com.google.zxing.EncodeHintType;
import com.google.zxing.MultiFormatWriter;
import com.google.zxing.Writer;
import com.google.zxing.client.j2se.MatrixToImageWriter;
import com.google.zxing.common.BitMatrix;
import com.google.zxing.qrcode.decoder.ErrorCorrectionLevel;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.awt.image.BufferedImage;
import java.util.HashMap;
import java.util.Map;

@Configuration
public class BarcodeConfig {

    /**
     * Создание генератора штрих-кодов формата Code-128
     * (стандарт для складского учета)
     */
    @Bean
    public Writer barcodeWriter() {
        return new MultiFormatWriter();
    }

    /**
     * Настройки по умолчанию для генерации штрих-кодов
     */
    @Bean
    public Map<EncodeHintType, Object> barcodeHints() {
        Map<EncodeHintType, Object> hints = new HashMap<>();
        hints.put(EncodeHintType.ERROR_CORRECTION, ErrorCorrectionLevel.L);
        hints.put(EncodeHintType.MARGIN, 2);
        hints.put(EncodeHintType.CHARACTER_SET, "UTF-8");
        return hints;
    }

    /**
     * Утилитарный метод для генерации изображения штрих-кода
     * Может быть использован для печати этикеток
     */
    public static BufferedImage generateBarcodeImage(String barcodeData, int width, int height) throws Exception {
        MultiFormatWriter writer = new MultiFormatWriter();
        Map<EncodeHintType, Object> hints = new HashMap<>();
        hints.put(EncodeHintType.MARGIN, 2);
        hints.put(EncodeHintType.CHARACTER_SET, "UTF-8");

        BitMatrix bitMatrix = writer.encode(barcodeData, BarcodeFormat.CODE_128, width, height, hints);

        return MatrixToImageWriter.toBufferedImage(bitMatrix);
    }
}