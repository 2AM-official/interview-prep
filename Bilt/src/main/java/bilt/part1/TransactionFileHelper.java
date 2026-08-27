package bilt.part1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

public final class TransactionFileHelper {
    private TransactionFileHelper() {}

    public static List<CSVRecord> parseFile(String classpathPath) throws IOException {
        String resource = classpathPath.startsWith("/") ? classpathPath.substring(1) : classpathPath;
        List<String> lines = readLines(resource);
        if (lines.isEmpty()) {
            return List.of();
        }

        String[] headers = split(lines.get(0));
        List<CSVRecord> records = new ArrayList<>();
        for (int i = 1; i < lines.size(); i++) {
            if (lines.get(i).isBlank()) {
                continue;
            }
            records.add(new CSVRecord(headers, split(lines.get(i))));
        }
        return records;
    }

    private static List<String> readLines(String resource) throws IOException {
        InputStream in = TransactionFileHelper.class.getClassLoader().getResourceAsStream(resource);
        if (in != null) {
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(in, StandardCharsets.UTF_8))) {
                return reader.lines().toList();
            }
        }
        Path[] candidates = new Path[] {
                Path.of("src/main/resources", resource),
                Path.of("Bilt/src/main/resources", resource)
        };
        for (Path path : candidates) {
            if (Files.isRegularFile(path)) {
                return Files.readAllLines(path, StandardCharsets.UTF_8);
            }
        }
        throw new IOException("CSV not found: " + resource);
    }

    private static String[] split(String line) {
        return line.split(",", -1);
    }
}

/** Minimal Commons-CSV compatible record so the starter code compiles without Maven. */
class CSVRecord {
    private final Map<String, String> values = new LinkedHashMap<>();

    CSVRecord(String[] headers, String[] fields) {
        for (int i = 0; i < headers.length; i++) {
            String header = headers[i].trim();
            String value = i < fields.length ? fields[i] : "";
            values.put(header, value);
            values.put(header.toUpperCase(Locale.ROOT), value);
        }
    }

    public String get(String name) {
        if (name == null) {
            return null;
        }
        String value = values.get(name);
        if (value != null) {
            return value;
        }
        return values.get(name.toUpperCase(Locale.ROOT));
    }
}
